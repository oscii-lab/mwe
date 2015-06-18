"""
wordnik_validation.py

Loads the top 10,000 results from the Linguee scraper, filters out the phrases,
and queries wordnik for definitions for each one. Any phrases (Multi-Word
Expressions) without a definition are written to the linguee_unique.csv file.
"""

from wordnik import *

SCRAPED_FILE_PATH = "../data/linguee_10000.csv"
UNIQUE_FILE_PATH = "../data/linguee_unique.csv"
API_URL = "http://api.wordnik.com/v4"
API_KEY_PATH = "../reference/key.secure"
API_KEY = ""
with open(API_KEY_PATH, 'r') as f:
    API_KEY = f.read().strip()

def extract_phrases():
    """Filters out and returns all multi-word expressions from scraped data."""
    with open(SCRAPED_FILE_PATH, 'r') as f:
        words = f.read().splitlines()
        return [w for w in words if len(w.split(" ")) > 1]

def query_wordnik(phrase):
    """Query wordnik for definition. Return phrase if no definition exists."""
    print phrase
    client = swagger.ApiClient(API_KEY, API_URL)
    wordApi = WordApi.WordApi(client)

    wiktionary = wordApi.getDefinitions(phrase, sourceDictionaries='wiktionary')
    wordnet = wordApi.getDefinitions(phrase, sourceDictionaries='wordnet')

    return True if (wiktionary is not None) or (wordnet is not None) else False

# Main
expressions = extract_phrases()
unique = [phrase for phrase in expressions if not query_wordnik(phrase)]

with open(UNIQUE_FILE_PATH, 'w') as f:
    for p in unique:
        f.write(p)
        f.write("\n")
