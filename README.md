# What is *code2semantics*?

Source code contains a lot more than just the logic structure. Developsers sometimes take a deep breath while having a coffee, when a new identifier* needs a good, precise and meaningful name. Have you ever had to read code, where identifiers were cryptic and not comprehensible at all? *code2semantics* aims to find those hotspots using Word2Vec machine learning models. It calculates semantic distances between identifiers and the overall file context. In more detail, this means, the project...

- extracts identifiers from source code using [antlr4](https://www.antlr.org)
- splits each identifier into separated words when using underscores or CamelCase notation
- extracts 16GB (4,600,000 wiki articles) of training data from [Wikipedia dumps](https://dumps.wikimedia.org/enwiki/latest/) *enwiki-latest-pages-articles.xml.bz2*
- trains the [Gensim](https://github.com/rare-technologies/gensim) Word2Vec model with the wikipedia training data
- evaluates the identifier words using the Word2Vec model

###### \* identifier can be a class name, method name, interface name or any other variable name, which can be set by the developer

## Requirements

- Install [Gensim](https://github.com/rare-technologies/gensim)

  `pip install -U gensim`

- Install [spaCy](https://github.com/explosion/spaCy) module and its english vocabulary

  `pip install -U spacy`
  
  `python -m spacy download en`

- Install the [antlr4](https://www.antlr.org) runnable and add it to the classpath. This allows using the predefined antlr4 parser

  ```
  cd /usr/local/lib
  sudo curl -O https://www.antlr.org/download/antlr-4.7.2-complete.jar
  export CLASSPATH=".:/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH"
  alias antlr4='java -jar /usr/local/lib/antlr-4.7.2-complete.jar'
  ```

## How to extract semantics from source code

- Extract identifiers and split those into words by underscore and CamelCase notation
  
  `python ProjectParser.py <file_or_directory_path>`

- Download the wikipedia dump (16GB) [enwiki-latest-pages-articles.xml.bz2](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2)
- Extract the articles text as training data from wikipedia dump (takes between 5-6 hours)
  
  `python WikiExtractor.py <<LANG>wiki-latest-pages-articles.xml.bz2>`
  
- Clean the wiki articles removing stopwords (use of nltk) and lemmatizing (use of spaCy) words

  `python TextCleaner.py <wiki.en.raw.txt>`

- Train a gensim Word2Vec model using train data (takes 5-6 hours for the raw wiki text)
  
  `python Word2VecTrainer.py <wiki.en.clean.txt>`
  
- Evaluate identifiers using the Word2Vec model. This currently just calculates the average semantic distance for each file between each identifier and the files context and creates a *CSV*-file containing the path and the overall semantic distance per file
  
  `python SemanticsCalculator.py <word2vec.model> <project_data.json>`

## How to add a new programming language with antlr4

### Generate Python classes for a new grammar
- Find the <new_language> grammar on [antlr-grammars-v4](https://github.com/antlr/grammars-v4)
- Create a new folder `<new_language>` inside `src/main/fileParser/`
- Copy paste all `.g4` files like Parser, Lexer or UnicodeClasses into the <new_language> folder
- Execute `antlr4 -Dlanguage=Python3 *.g4` inside your <new_language> folder. This generates some Python3 classes and other files.

### Override generated listener methods
- Create a new file `<new_language>ListenerExtended.py` inside `src/main/fileParser/ExtendedListener/`
- Create a new class which just looks similar to the other existing classes like `JavaParserListenerExtended` and extend the BaseListener class
- Every grammer is potentiall different. That's why you need to have a look into the `<your_language>Parser.g4` file and find the appropriate class, method, variable and general identifier declarartion.
- The Listener function names always match up with the grammar rule-name. Override the Listener functions and store the obtained values inside the predefined BaseListener variables.

### Walk through the new grammar
- Create another function inside the `src/main/filerParser/LanguageParser` and substitute your generated/created classes like shown below

    ```python
    def parse_<your_language>_file(self, input_stream: InputStream):
        lexer = <your_generated_lexer>(input_stream)
        stream = CommonTokenStream(lexer)
        parser = <your_generated_parser>(stream)
        tree = parser.<your_top_level_grammar_node>()
        listener = <your_expanded_listener>()
        return self.walk(listener, tree)
    ```
### Add your supported language extension
- Inside `src/main/fileParser/Lanague.py` an enum with all supported programming languages is stored. Add your language name with its file-extension.


### Add new option use your parse_<your_language>_file function
- The `LanguageParser.parse_file()` function calls the appropriate parsing function for each language. Add yours with another if-statement


