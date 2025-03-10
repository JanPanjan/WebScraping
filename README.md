# Webscraping with Python

Goal: use webscraping to scrape eservis website for appropriate študentska dela.

---

## Typical procces for webscraping

1. **Inspection of the website** - use browser's developer tools (F12) to examine HTML structure of
the website. Identify HTML tags and attributes that contain the data you want to extract.

2. **Send HTTP request to the server** - use requests library to send a GET request to the server and
retrieve the HTML content of the website.

3. **Parse the HTML content** - use BeautifulSoup library to create a parse tree from the HTML content.

4. **Extract the data** - use beautifulsoup methods to extract the data from the parse tree, e.g. find(),
find_all(), select(), etc.

5. **Store the data** - save scraped data to a file or database for further analysis.

For learning purposes we are going to scrape the next websites. They are easy to scrape and don't 
require any authentication. They are relatively simple and we don't have to worry about getting
blocked by the server by scraping the website:
* http://quotes.toscrape.com/
* http://books.toscrape.com/
* https://en.wikipedia.org/wiki/Generative_adversarial_network
* https://fakestoreapi.com/
