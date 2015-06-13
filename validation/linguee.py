"""
linguee.py

Simple scraper script to get the top 10,000 most popular words/phrases searched
for by Linguee users.
"""

from bs4 import BeautifulSoup
import urllib2

BASE_URL = "http://www.lingue.com"

# URL with links to all of the top 10,000 Linguee words/phrases
SEARCH_SUB_URL = "/english-german/topenglish/1-10000.html"

def get_sub_pages():
    """Returns a list of sub-urls where the data is located."""
    response = urllib2.urlopen(BASE_URL + SEARCH_SUB_URL)
    html = response.read()

