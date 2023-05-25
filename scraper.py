import requests
from bs4 import BeautifulSoup

# Make a request to the website
r = requests.get(
    "https://www.cnn.com/2023/05/25/us/brian-laundrie-mother-letter-gabby-petito/index.html")

# Parse the HTML content
soup = BeautifulSoup(r.text, 'html.parser')

# Find the main headlines
headlines = soup.find_all(class_='article__content')

for headline in headlines:
    print(headline.get_text())
