import requests
from bs4 import BeautifulSoup


# Scraper for website = requests.get('http://quotes.toscrape.com/')
# soup = BeautifulSoup(website.text, 'html.parser')
next_button = True
page = 1
# print(next_button)

while next_button:
    website = requests.get('http://quotes.toscrape.com/page/' + str(page))
    soup = BeautifulSoup(website.text, 'html.parser')
#     ## Using HTML tags
#     # website_title = soup.find('title')
#     link_title = soup.find('a')
#     login_link = soup.find(href='/login')
#     # print(login_link)
#     # quotes = soup.find_all(class_='quote')
#     # for quote in quotes:
#     #     text = quote.find(class_='text')
#     #     author = quote.find(class_='author')
#     #     print(text.text, author.text)
#     #
#     # h2 = soup.select_one('h2')
#     # print(h2.text)
#
    ## Using CSS Selectors
    quotes_css = soup.select('.quote')
    for quote in quotes_css:
        quote_text = quote.select_one('.text')
        author = quote.select_one('.author')
        print(quote_text.text, author.text)
        tags_css = quote.select('.tag')
        print('<' * 10 + ' Tags ' + '>' * 10)
        for tag in tags_css:
            print(tag.text)
        print('=' * 100)
    print("Page: " + str(page))
    next_button = soup.select_one('.next > a')
    page += 1


