import requests
from bs4 import BeautifulSoup

website = requests.get("https://www.britannica.com/biography/William-of-Moerbeke")
soup = BeautifulSoup(website.text, "html.parser")

name = soup.select_one('h1').text
summary = soup.select_one('.topic-identifier').text

try:
    image = soup.select_one('.qf-module img').attrs['src']
except AttributeError as error:
    image = None

facts_from_sidebar = soup.select('dl.js-fact')
birth_facts = facts_from_sidebar[0]
death_facts = facts_from_sidebar[1]

try:
    birth_date = birth_facts.find('dd').get_text('|').strip().split('|')[1]
except AttributeError as error:
    birth_date = None

try:
    death_date = death_facts.find('dd').get_text('|').strip().split('|')[1]
except AttributeError as error:
    death_date = None

try:
    subject_items = soup.select_one('dl.js-fact.mb-0.position-relative.clamp-3').find('dd').select('a')
    subjects_of_study = ''
    for item in subject_items:
        subjects_of_study += item.text + ', '
except AttributeError as error:
    subjects_of_study = None

print(f'{name}\n{summary}\n{birth_date}\n{death_date}\n{subjects_of_study}')


















# import requests
# from bs4 import BeautifulSoup
#
# # website = requests.get('https://www.britannica.com/biography/Mortimer-J-Adler')
# website = requests.get('https://www.britannica.com/biography/William-of-Moerbeke')
# soup = BeautifulSoup(website.text, 'html.parser')
#
# name = soup.select_one('h1').text
# summary = soup.select_one('.topic-paragraph').text
# try:
#     image = soup.select_one('.fact-box-picture img').attrs['src']
# except AttributeError as error:
#     image = None
# birth_date = soup.find(attrs={'data-label': 'born'}).find('dd').get_text(separator='|').split('|')[0]
# death_date = soup.find(attrs={'data-label': 'died'}).find('dd').get_text(separator='|').split('|')[0]
# try:
#     subject_items = soup.find(attrs={'data-label': 'subjects of study'}).select('ul > li')
#     subjects = ''
#     for item in subject_items:
#         subjects += item.text.strip() + ', '
# except AttributeError as error:
#     subjects = None
#
# print(f"{name}\n{summary}\n{image}\n{birth_date}\n{death_date}\n{   subjects}")
