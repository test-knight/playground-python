# Wikipedia Population Parser
# https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population
import requests
from bs4 import BeautifulSoup
import csv

website = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population")
soup = BeautifulSoup(website.text, 'html.parser')
table = soup.select_one('.wikitable')
rows = table.select('tr')[1:-1]
csv_data = [['rank', 'country', 'region', 'population', 'percentage', 'date', 'source']]

for row in rows:
    rank = row.find('th').text.strip()
    # try:
    table_data = row.select('td')

    index = 0
    try:
        country = table_data[index].find('a').text.strip()
        region, index = table_data[index+1].text, index+1
    except AttributeError as error:
        country = table_data[0].find('b').text.strip()
        region = None

    population, index = table_data[index+1].text, index+1
    percentage, index = table_data[index+1].text, index+1
    date, index = table_data[index+1].text, index+1
    source = table_data[index+1].text.strip().split("[")[0]
    print(f"Rank: {rank}; Country: {country}; Region: {region}; Population: {population}; Percentage: {percentage}; Date: {date}; Source: {source}")
    csv_data.append([rank, country, region, population, percentage, date, source])

with open("countries_population_list.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
