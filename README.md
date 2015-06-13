##Multiword Expressions and Multiword Segmentation##

The goal of this project is to be able to automatically and efficiently detect the existence of multiword expressions in text, by building upon existing models of segmentation. We will do this by introducing several user-defined data sources in which such expressions are defined, with the hope that this will increase accuracy.

###Background###

The underlying model that this is built off of is Nathan Schneider's PhD Thesis, "Lexical Semantic Analysis in Natural Language Text", which is included in the above directory. For the purposes of this project, we assume his definition of a multi-word expression, as follows:

**Multiword Expressions (MWEs)**: Lexicalized combinations of two or more words that are exceptional enough to be considered as single units in the lexicon. 

Although slightly vague, this definition is expanded upon in Schneider's thesis (Chapter 3, pg. 29), with several examples of common classes of idiomatic language in English.

In Schneider's Thesis, he cites both Wordnet and Wiktionary as data sources that he trains his model off of (in addition to a set of other linguistic cues). While both of these sources are good tools for finding common idiomatic expressions, they are by no means comprehensive. Thus we suggest the following series of steps, to improve the accuracy and efficiency of devloping a model for identify multiword expressions in text.

###Step 1: Validation###

First, we introduce [Linguee](http://www.linguee.com/) as an additional source of data for finding multiword expressions. While it's primary feature is that of language translation, Linguee also offers a frequency-ordered list of the most common phrases that are searched for by users of the site (including idiomatic phrases). It is our hope that the 1,000,000 or so entries in the Linguee dataset provide some additional information (more idiomatic phrases) for use in the identification process. To ensure that this is the case, the first step is to validate the Linguee data, in the following manner:

1. Scrape Linguee for the first 10,000 phrases/words.
2. Of the elements in the scraped set that are multi-word expressions (phrasal in nature), query Wordnet + Wiktionary (via [Wordnik](https://www.wordnik.com/)) for their existence.
3. Take some top *k* elements that are unique to Linguee, and hand validate them against Schneider's definition. If they meet the definition of an MWE, then this shows promise as a potential datasource.

To run the above validation process, we will use the following (preliminary) directory structure. 

```
.
├── validation
|   ├── linguee.py
|   └── wordnik_parser.py
├── data
|   ├── linguee_10000.csv
|   └── linguee_unique.csv
├── reference
|   └── schneider.pdf
└── README.md
```
