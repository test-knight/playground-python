import requests
from bs4 import BeautifulSoup

page = 1
next_button = True

while next_button:
    website = requests.get(f'https://quotes.toscrape.com/page/{page}/')
    soup = BeautifulSoup(website.text, 'html.parser')

    quotes = soup.find_all(class_='quote')
    next_button = soup.select_one('.next > a')

    for quote in quotes:
        saying = quote.find(class_='text')
        author = quote.find(class_='author')
        tags = quote.find_all(class_='tag')
        tags_per_saying = []
        print(f"Quote: {saying.text}, by {author.text}")
        for tag in tags:
            tags_per_saying.append(tag.text)
        # print(*tags_per_saying)
        print("Tags: #" + ", #".join(str(x) for x in tags_per_saying))
        print("-" * 50)
    print(f"End of Page: {page}")
    print("#" * 50)
    page += 1
