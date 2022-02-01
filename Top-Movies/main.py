from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, "html.parser")

ranking_details = soup.find_all(name="img", class_="landscape")

rankings = [ranking_detail.get("title") for ranking_detail in ranking_details]
rankings.reverse()

with open('movies.txt', 'w') as f:
    for item in rankings:
        f.write("%s\n" % item)

