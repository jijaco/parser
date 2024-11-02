import requests
import json
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"
req = requests.get(url)

soup = BeautifulSoup(req.text, "lxml")

all_div = soup.find_all("div", class_="quote")
all_quotes = [div.find("span", class_="text") for div in all_div]
all_authors = [div.find("small", class_="author") for div in all_div]

quotes: dict = [{"quote": quote.contents[0], "author": author.contents[0]}
                for quote, author in zip(all_quotes, all_authors)]

with open("quotes.json", "w") as f:
    json.dump(quotes, f)
