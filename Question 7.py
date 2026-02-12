"""
Question 7

In this question, you will work on extracting structured content from a webpage using Beautiful-
Soup.
Scrape the Wikipedia page:
https://en.wikipedia.org/wiki/Data_science
Write a program using requests and BeautifulSoup that:
• Extracts and prints the page title from the <title> tag.
• Extracts the first paragraph from the main article content inside the div with id mw-
content-text.
• The paragraph must contain at least 50 characters (after stripping whitespace)

"""
from bs4 import BeautifulSoup
import requests

data_science_wikipedia_page = requests.get(
    "https://en.wikipedia.org/wiki/Data_science",
    headers={"User-agent": "DATA221-Assignment/1.0a (dominic.deramos@ucalgary.ca)"}
)
parsed_webpage = BeautifulSoup(data_science_wikipedia_page.content, "html5lib")


# 1.) Extracts and prints the page title from the <title> tag.
page_title = parsed_webpage.find("title").text
print(page_title)


# 2.) Extracts the first paragraph from the main article content inside the div with id mw-
# content-text.
main_article_content = parsed_webpage.find("div", id="mw-content-text")
first_paragraph = main_article_content.find_all("p")


# 3.) The paragraph must contain at least 50 characters (after stripping whitespace)
for p in first_paragraph:
    text = p.get_text(strip=True)
    if len(text) >= 50:
        print("\nFirst valid paragraph:")
        print(text)
        break