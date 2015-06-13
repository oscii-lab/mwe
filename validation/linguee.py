"""
linguee.py

Simple scraper script to get the top 10,000 most popular words/phrases searched
for by Linguee users.
"""

from bs4 import BeautifulSoup
import urllib2

BASE_URL = "http://www.linguee.com"
data_file = "../data/linguee_10000.csv"

# URL with links to all of the top 10,000 Linguee words/phrases
SEARCH_SUB_URL = "/english-german/topenglish/1-10000.html"

def get_sub_pages():
    """Returns a list of sub-urls where the data is located."""
    response = urllib2.urlopen(BASE_URL + SEARCH_SUB_URL)
    html = response.read()

    soup = BeautifulSoup(html)
    url_tags = [tag.find('a') for tag in soup.find_all('td')]
    return [url.get('href') for url in url_tags if url is not None]

def get_words(sub_urls):
    """Parses the words from each sub-url, returns them as a list."""
    word_list = []

    for url in sub_urls:
        response = urllib2.urlopen(BASE_URL + url)
        html = response.read()

        soup = BeautifulSoup(html)
        word_tags = [tag.find('a').text for tag in soup.find_all('td')]
        word_list.extend(word_tags)
        print("Finishing %s" % (url))

    return word_list

def write_results(word_list):
    """Writes the list of top 10,000 words to file."""
    with open(data_file, 'w') as f:
        for word in word_list:
            f.write(word)
            f.write("\n")

# Main
words = get_words(get_sub_pages())
write_results(words)



