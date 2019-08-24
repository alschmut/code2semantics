## Jump to Section

* [What is *code2semantics*?](#what-is-code2semantics)
* [Target Languages](#target-languages)
* [Installation Requirements](#installation-requirements)
* [How to get a Word2Vec model using Wikipedia data](#how-to-get-a-word2vec-model-using-wikipedia-data)
* [How to extract semantics from source code](#how-to-extract-semantics-from-source-code)
* [How to add a new programming language with antlr4](#how-to-add-a-new-programming-language-with-antlr4)


# What is *code2semantics*?

Source code contains a lot more than just the logic structure. Developers sometimes take a deep breath while having a coffee, when a new identifier* needs a good, precise and meaningful name. Have you ever had to read code, where identifiers were cryptic and not comprehensible at all? *code2semantics* aims to find those hotspots using Word2Vec machine learning models. It calculates semantic distances between identifiers and the overall file context. In more detail, this means, the project...

- extracts identifiers from source code using [antlr4](https://www.antlr.org)
- splits each identifier into separated words when using underscores or CamelCase notation
- extracts 16GB (4,600,000 wiki articles) of training data from [Wikipedia dumps](https://dumps.wikimedia.org/enwiki/latest/) *enwiki-latest-pages-articles.xml.bz2*
- trains the [Gensim](https://github.com/rare-technologies/gensim) Word2Vec model with the wikipedia training data
- evaluates the identifier words using the Word2Vec model and creates multiple identifier metrics

###### \* identifier can be a class name, method name, interface name or any other variable name, which can be set by the developer



## Target Languages

- Java
- Kotlin

## Simple example of what code2semantics does
1.  Given this source code:
    ```
    1 public class Foo {
    2     private String fooBar;
    3
    4     private setFooBar(String fooBar) {
    5         this.fooBar = fooBar;
    6     }
    7 }
    ```

1.  Parses and extract each declared identifier together with its line number:

    |identifier|line
    |---|---
    |foo        |1
    |fooBar     |2
    |setFooBar  |4
    |fooBar     |5

1.  Separate each identifier by Camel Case and underscore notation into individual words:

    |unique identifier  |frequency  |words
    |---                |---        |---
    |foo                |1          |foo
    |fooBar             |2          |foo, bar
    |setFooBar          |1          |set, foo, bar

1.  List all unique words:

    |word   |frequency
    |---    |---
    |foo    |4
    |bar    |3
    |set    |1

1. Generate metrics for each word
1. Aggregate each word metric (summarize or aggregate) to represent the identifier metric

## Generated metrics per identifier
The results of the parsed source code will be exported as custom *.c2s.json* file as well as a *.csv* table containing all generated metrics:

|metric                             |type       |description
|---                                |---        |---
|`distance_to_class_name`           |relative   |cosine distance between identifier and its class-name\* mulitplied by 100
|`distance_to_file_context`         |relative   |cosine distance between identifier and its file-context\* mulitplied by 100
|`identifier_frequency_per_file`    |absolute   |cumulative number of occurences of an identifier in its file
|`identifier_length`                |absolute   |number of characters of an identifier
|`number_of_separated_words`        |absolute   |number of individual words inside an identifier
|`percent_of_word2vec_words`        |relative   |percent of words in an identifier that are stored inside the Word2Vec model
|`word_frequency_per_file`          |absolute   |cumulative number of occurences of a word of an identifier in its file

###### \* a class name vector is the most similar vector to all words in a class name and the file-context is the most similar vector to all individual words inside a class.


## Installation Requirements
Depending on what you have already installed you might need to install more or less of the following list:
- Install python3 (including pip3)

  `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
  
  `brew install python`
  
- Install the [SciPy](https://www.scipy.org/install.html) stack (gensim makes use of those)

  `python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose`

- Install [Gensim](https://github.com/rare-technologies/gensim)

  `pip3 install -U gensim`

- Install [spaCy](https://github.com/explosion/spaCy) module and its english vocabulary

  `pip3 install -U spacy`
  
  `python3 -m spacy download en`

- Download the NLTK python tool kit together with its english stopword list

  ```
  pip3 install nltk 
  python3
  >>> import nltk
  >>> nltk.download('stopwords')
  ```

- Install the [antlr4](https://www.antlr.org) runnable and add it to the classpath. This allows using the predefined antlr4 parser

  ```
  cd /usr/local/lib
  sudo curl -O https://www.antlr.org/download/antlr-4.7.2-complete.jar
  export CLASSPATH=".:/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH"
  alias antlr4='java -jar /usr/local/lib/antlr-4.7.2-complete.jar'
  pip install antlr4-python3-runtime
  ```

## How to get a Word2Vec model using Wikipedia data

The Word2Vec model is a vector space model storing word with a semantic relatendess. This model is needed for the following step analyzing the source code data.

- Download the wikipedia dump (16GB) [enwiki-latest-pages-articles.xml.bz2](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2)
- Extract the articles text as training data from wikipedia dump (takes between 5-6 hours)
  
  `python WikiExtractor.py <enwiki-latest-pages-articles.xml.bz2>`
  
- Remove nltk-stopwords from the wiki articles (takes 8 minutes)

  `python TextStopwordFilter.py <wiki.en.raw.txt>`

- Lemmatize the words using of spaCy inside the wiki articles (takes 7-8 hours)

  `python TextLemmatizer.py <wiki.en.filtered.txt>`

- Train a gensim Word2Vec model using train data (takes 2:30 hours)
  
  `python Word2VecTrainer.py <wiki.en.lemmatized.txt>`

## How to extract semantics from source code

- Extract identifiers and split those into words by underscore and CamelCase notation. If the optional Word2Vec model (as binary or not) is provided, it analyzes each word using the semantic relatedness to its class name and its file-context.
  
  `python ProjectParser.py <file_or_directory_path> [<word2vec.model>]`
  


## Useful links for pre-trained Word2Vec models
- Google provides a 1.5GB Word2Vec model and describes its vocabulary in [this Blog post](http://mccormickml.com/2016/04/12/googles-pretrained-word2vec-model-in-python/) and can be downloaded from [Google Drive](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing). In short: 
  - The data is obtained from 100 billion words from a Google News dataset
  - The vocabulary includes many stopwords
  - words are not lemmatized
- A list of pre-trained models from different sources is provided on a [3Top GitHub project](https://github.com/3Top/word2vec-api).



## How to add a new programming language with antlr4

### Generate Python classes for a new grammar
- Find the <new_language> grammar on [antlr-grammars-v4](https://github.com/antlr/grammars-v4)
- Create a new folder `<new_language>` inside `src/main/antlrParser/`
- Copy paste all `.g4` files like Parser, Lexer or UnicodeClasses into the <new_language> folder
- Execute `antlr4 -Dlanguage=Python3 *.g4` inside your <new_language> folder. This generates some Python3 classes and other files.

### Override generated listener methods
- Create a new file `<new_language>ListenerExtended.py` inside `src/main/antlrParser/ExtendedListener/`
- Create a new class which just looks similar to the other existing classes like `JavaParserListenerExtended` and extend the BaseListener class
- Every grammer is potentiall different. That's why you need to have a look into the `<your_language>Parser.g4` file and find the appropriate class, method, variable and general identifier declarartion.
- The Listener function names always match up with the grammar rule-name. Override the Listener functions and store the obtained values inside the predefined BaseListener variables.

### Walk through the new grammar
- Create another function inside the `src/main/antlrParser/LanguageParser` and substitute your generated/created classes like shown below

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
- Inside `src/main/antlrParser/Lanague.py` an enum with all supported programming languages is stored. Add your language name with its file-extension.


### Add new option to use your parse_<your_language>_file function
- The `LanguageParser.parse_file()` function calls the appropriate parsing function for each language. Add yours with another if-statement


