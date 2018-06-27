# textcat-in-python

This project is implementation of paper on language classification by Cavner and Trenkle (1994) in python.
Given an input file in a particular language , it will classify the language into one of following languages.

'Bulgarian', 'Czech', 'Swedish', 'German', 'Greek', 'English', 'Spanish', 'Estonian', 'Finnish', 'French', 'Hungarian', 'Italian', 'Lithuanian', 'Latvian', 'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Slovak', 'Slovenian', 'Norwegian'

**Note** : input text should be larger than order of 100 characters.

Please clone the repo and use below commands to classify a text.

## Usage
```
python main.py <path/to/text/file>
```
Example:
```
python main.py example\french.txt
```

## References

1. Cavnar, William B. and John M. Trenkle. "N-Gram-Based Text Categorization". Proceedings of SDAIR-94, 3rd Annual Symposium on Document Analysis and Information Retrieval (1994)
2. Europarl: A Parallel Corpus for Statistical Machine Translation, Philipp Koehn, MT Summit 2005
