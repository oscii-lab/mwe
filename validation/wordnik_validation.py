"""
wordnik_validation.py

Loads the top 10,000 results from the Linguee scraper, filters out the phrases,
and queries wordnik for definitions for each one. Any phrases (Multi-Word
Expressions) without a definition are written to the linguee_unique.csv file.
"""

SCRAPED_FILE_PATH = "../data/linguee_10000.csv"

def extract_phrases():
    """Filters out and returns all multi-word expressions from scraped data."""
    with open(SCRAPED_FILE_PATH, 'r') as f:
        words = f.read().splitlines()
        return [w for w in words if len(w.split(" ")) > 1]



# Main
expressions = extract_phrases()