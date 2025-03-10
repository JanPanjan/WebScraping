import pprint
import requests # HTTP requests

from bs4 import BeautifulSoup # HTML parsing

import selenium # Web automation
import playwright # Web automation

"""
Typical procces for webscraping:

1. Inspection of the website - use browser's developer tools (F12) to examine HTML structure of
the website. Identify HTML tags and attributes that contain the data you want to extract.

2. Send HTTP request to the server - use requests library to send a GET request to the server and
retrieve the HTML content of the website.

3. Parse the HTML content - use BeautifulSoup library to create a parse tree from the HTML content.

4. Extract the data - use beautifulsoup methods to extract the data from the parse tree, e.g. find(),
find_all(), select(), etc.

5. Store the data - save scraped data to a file or database for further analysis.

For learning purposes we are going to scrape the next websites. They are easy to scrape and don't 
require any authentication. They are relatively simple and we don't have to worry about getting 
blocked by the server by scraping the website:
* http://quotes.toscrape.com/
* http://books.toscrape.com/
* https://en.wikipedia.org/wiki/Generative_adversarial_network
* https://fakestoreapi.com/

"""

def perform_request(url: str) -> requests.models.Response:
    """
    Sends a get request to the server. Checks the status code of the response. Status codes are 
    3-digit numbers that web serves use to communicate the outcome of the HTTP request (200 - OK, 
    404 - Not Found, 403 - Forbidden, 500 - Internal Server Error, etc.)
    * 2xx - Successful requests
    * 3xx - Redirection (further action needed to complete request)
    * 4xx - Client Error (request can't be fulfilled due to your code)
    * 5xx - Server Error (server failed to fulfill a valid request)
    If it returns a bad code, we raise an exception.

    Args:
        url (str): The URL of the website to scrape.
    Returns:
        response (requests.models.Response): The response object returned by the server.
    """
    response = requests.get(url)
    response.raise_for_status()

    return response


def scrape_quotes(url: str, n=None):
    """
    Scrapes quotes from the given URL.

    Args:
        url (str): The URL of the website to scrape.
        n (int): The number of quotes to scrape. If None, scrape all quotes.
    Returns:
        quotes_formatted (dict): A dictionary containing the scraped quotes.
    """
    response = perform_request(url)
    soup = BeautifulSoup(response.content, "lxml")
    quotes = soup.find_all(name="div", attrs="quote")

    quotes_formatted = {}

    if n is None:
        n = len(quotes)

    for i in range(n):
        quote = quotes[i]
        quotes_formatted[i] = parse_quote(quote)
    
    return quotes_formatted


def parse_quote(quote) -> dict:
    """
    Parses the given quote. It's important to study the HTML structure of the
    website to know how to extract the data.

    Args:
        url (str): The URL of the website to scrape.
    Returns:
        (dict): A dictionary containing the scraped quote
    """
    quote_text = quote.find(name="span", attrs="text").text.strip()
    quote_author = quote.find(name="small", attrs="author").text.strip()
    quote_tags = quote.find(name="div", attrs="tags")
    quote_tags = [tag.text.strip() for tag in quote_tags.find_all(name="a", attrs="tag")]

    return {
        "quote": quote_text, 
        "author": quote_author, 
        "tags": quote_tags
    }


def main():
    quotes_url = "http://quotes.toscrape.com/"
    books_url = "http://books.toscrape.com/"
    wiki_url = "https://en.wikipedia.org/wiki/Generative_adversarial_network"
    fakestore_url = "https://fakestoreapi.com/"

    first_three_quotes = scrape_quotes(quotes_url, 3)
    [pprint.pprint(quote) for quote in first_three_quotes.values()]
    

if __name__ == "__main__":
    main()
