import requests
from bs4 import BeautifulSoup
import csv

header = {"Accept-Language": "en-US"}
# website = requests.get("https://www.imdb.com/title/tt0770828/", headers=header)
website_top250 = requests.get("https://www.imdb.com/chart/top", headers=header)
soup_top250 = BeautifulSoup(website_top250.text, 'html.parser')
links = soup_top250.select('.lister-list  .titleColumn a')
csv_data = [['movie_name', 'release_year', 'genre', 'rating', 'running_time', 'imdb_rating', 'director', 'plot', 'casts']]

for link in links:
    movie_link = link.attrs['href']
    website_movie = requests.get(f'https://www.imdb.com{movie_link}', headers=header)
    soup = BeautifulSoup(website_movie.text, 'html.parser')

    def get_tag(id: str):
        return soup.find(attrs={'data-testid': id})

    def get_tags(id: str):
        return soup.find_all(attrs={'data-testid': id})


    movie_name = get_tag('hero-title-block__title').text
    meta_data = get_tag('hero-title-block__metadata').contents
    release_year = meta_data[0].find('span').text.strip()
    rating = meta_data[1].find('span').text.strip()
    running_time = meta_data[2].text.strip()
    plot = get_tag('plot-xl').text.strip()
    imdb_rating = get_tag('hero-rating-bar__aggregate-rating__score').text.strip()
    director = get_tag('title-pc-principal-credit').select_one('div').text.strip()

    genres_data = get_tag('genres').contents
    genres = ''
    for item in genres_data:
        genres += item.find('span').text.strip() + ', '
    genres = genres[:-2]

    cast_data = get_tags('title-cast-item__actor')
    casts = ''
    for item in cast_data[:5]:
        casts += item.text.strip() + ', '
    casts = casts[:-2]

    csv_data.append([movie_name, release_year, genres, rating, running_time, imdb_rating, director, plot, casts])
    print(f"Movie: {movie_name}; Release Year: {release_year}; Genres: {genres}; Rating: {rating}; "
          f"Running Time: {running_time}; IMDB Rating: {imdb_rating}; Director: {director}; Plot: {plot}; Casts: {casts}")


with open("imdb_movie_list_scraped.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
