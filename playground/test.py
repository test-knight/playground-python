import requests
from bs4 import BeautifulSoup
import csv

website = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population")
soup = BeautifulSoup(website.text, features='html.parser')
csv_data = [['rank', 'name', 'population', 'percentage', 'date_recorded', 'source']]

table = soup.select_one('.wikitable')
rows = table.select('tbody > tr')
for row in rows[1:-1]:
    rank = row.find('th').text.strip()
    table_data = row.select('td')
    name = table_data[0].select_one('a').text
    population = table_data[1].text
    percentage = table_data[2].text
    date_recorded = table_data[3].text
    source = table_data[4].get_text(',').split(',')[0]
    csv_data.append([rank, name, population, percentage, date_recorded, source])

with open('countries_population_list.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(csv_data)
