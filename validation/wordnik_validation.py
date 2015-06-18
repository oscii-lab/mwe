"""
wordnik_validation.py

Loads the top 10,000 results from the Linguee scraper, filters out the phrases,
and queries wordnik for definitions for each one. Any phrases (Multi-Word
Expressions) without a definition are written to the linguee_unique.csv file.
"""