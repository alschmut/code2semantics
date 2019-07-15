# What is *code2semantics*?

Source code contains a lot more than just the logic structure. Developsers sometimes take a deep breath while having a coffee, when a new identifier needs a good, precise and meaningful name. Have you ever had to read code, where identifiers were cryptic and not comprehensible at all? *code2semantics* aims to find those hotspots using Word2Vec machine learning models. It calculates semantic distances between identifiers and the overall file context. In more detail, this means, the project...

- extracts identifiers from source code using [antlr4](https://www.antlr.org)
- splits each identifier into separated words when using underscores or CamelCase notation
- extracts 16GB (4,600,000 wiki articles) of training data from [Wikipedia dumps](https://dumps.wikimedia.org/enwiki/latest/) *enwiki-latest-pages-articles.xml.bz2*
- trains the [Gensim](https://github.com/rare-technologies/gensim) Word2Vec model with the wikipedia training data
- evaluates the identifier words using the Word2Vec model

## Requirements

- Install [Gensim](https://github.com/rare-technologies/gensim)

  `pip install -U gensim`

- Install the antlr4 runnable and add it to the classpath. This allows using the predefined antlr4 parser

  ```
  cd /usr/local/lib
  sudo curl -O https://www.antlr.org/download/antlr-4.7.2-complete.jar
  export CLASSPATH=".:/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH"
  ```

## How to extract semantics from source code

- Extract identifiers and split into words by underscore
  
  `python FileParser.py <file_or_directory_path>`

- Download the wikipedia dump (16GB) [enwiki-latest-pages-articles.xml.bz2](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2)
- Extract the articles text as training data from wikipedia dump (takes between 5-6 hours)
  
  `python WikiExtractor.py <<LANG>wiki-latest-pages-articles.xml.bz2>`
  
- Train Word2Vec model using train data (takes 5-6 hours for the raw wiki text)
  
  `python Word2VecTrainer.py <wiki.<LANG>.text>`
  
- Evaluate identifiers using the Word2Vec model. This currently just calculates the average semantic distance for each file between each identifier and the files context and creates a *CSV*-file containing the path and the overall semantic distance per file
  
  `python SemanticsCalculator.py <word2vec.model> <project_data.json>`

