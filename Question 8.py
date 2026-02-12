"""
Question 8

This task focuses on extracting structured heading information from a webpage.
Using the same Wikipedia page:
https://en.wikipedia.org/wiki/Data_science
• Extract all <h2> section headings from the main content area (div with id mw-content-
text).
• Do not include headings containing the words: References, External links, See also, or
Notes.
• Remove any [edit] text from headings.
• Save the headings to headings.txt, one per line, in order.

"""
from bs4 import BeautifulSoup
import requests

data_science_wikipedia_page = requests.get(
    "https://en.wikipedia.org/wiki/Data_science",
    headers={"User-agent": "DATA221-Assignment/1.0b (dominic.deramos@ucalgary.ca)"}
)
parsed_webpage = BeautifulSoup(data_science_wikipedia_page.content, "html5lib")


# 1.) Extract all <h2> section headings from the main content area (div with id mw-content-
# text).
main_article_content = parsed_webpage.find("div", id="mw-content-text")
h2_headings = main_article_content.find_all("h2")


headings_list = []
exclude_words = ["References", "External links", "See also", "Notes"]


# 2.) Remove any [edit] text from headings.
for h2 in h2_headings:
    heading_text = h2.get_text(strip=True).replace("[edit]", "")


# 3.) Do not include headings containing the words: References, External links, See also, or
    # Notes.
    if any(word in heading_text for word in exclude_words):
        continue

    headings_list.append(heading_text)


# 4.) Save the headings to headings.txt, one per line, in order.
with open("headings.txt", "w", encoding="utf-8") as f:
    for heading in headings_list:
        f.write(heading + "\n")

print("Headings saved to headings.txt")