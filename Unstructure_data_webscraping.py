from bs4 import BeautifulSoup
import requests
import pandas as pd

def run():
    url = "https://www.imdb.com/chart/top/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # scrap movie names
    scraped_movies = soup.find_all('td', class_='titleColumn')
    # parse movie names
    movies = []
    for movie in scraped_movies:
        movie = movie.get_text().replace('\n', "")
        movie = movie.strip(" ")
        movies.append(movie)
    # scrap rating for movies
    scraped_ratings = soup.find_all('td', class_='ratingColumn imdbRating')
    # parse ratings
    ratings = []
    for rating in scraped_ratings:
        rating = rating.get_text().replace('\n', '')
        ratings.append(rating)
    data = pd.DataFrame()
    data['Movie Names'] = movies
    data['Ratings'] = ratings
    data.to_csv('imdp_top_Movies.csv', index=False)

if __name__ =="__main__":
    run()