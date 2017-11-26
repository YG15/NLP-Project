################################################
# Name: Gutenberg_text_scrapper
# Author: Yonathna Guttel
# Purpose: Recieves the number of a corpus in the English Gutenberg project and return in as a plain txt
# Arguments: an integer representing the corpus numbe in Gutenberg project (for more details see: http://www.gutenberg.org/browse/languages/en)
# Returning: a text string with the whole corpus
# Date: 26.11.2017
# Version: 1
##############################################
import requests
from bs4 import BeautifulSoup


def get_scrap(cor_num):

    # Creates the appropriate url to get to the book
    url = 'https://www.gutenberg.org/files/{0}/{0}-h/{0}-h.htm'.format(str(cor_num))

    # Tests if the book exist in Gutenberg project
    request = requests.get(url)
    if request.status_code != 200:
        print('Corpus does not exist')

    # Make the request
    r = requests.get(url)

    # Extract HTML from Response object
    ########should be later improved not to take all the extra stuff in the begining and end of the book- but only the story itself
    html = r.text

    # Create a BeautifulSoup object from the HTML
    soup = BeautifulSoup(html, "html5lib")

    # Get soup title as string and print a message to console
    C_title = soup.title.string
    print ("Succefuly picked: ",C_title)

    # Get the text out of the soup
    text = soup.get_text()

    return (text)
