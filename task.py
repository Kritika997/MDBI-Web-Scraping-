import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

IMDB_url = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
get_url = requests.get(IMDB_url)
soup = BeautifulSoup(get_url.text,"html.parser")

movies_dic = {}
movies_list = []
def scrape_top_list():
    all_movie_name = soup.find("div",class_="seen-collection")
    heading_1 = all_movie_name.find("div",class_="article").h3.get_text()
    heading_2 = all_movie_name.find("div",class_="article").h1.get_text()
    a = all_movie_name.find("div",class_="lister")
    b = a.find("tbody",class_="lister-list")
    trs_tags = b.find_all("tr")
    pos_num = 0
    for i in trs_tags:
        movie_title = i.find("td",class_="titleColumn").a.get_text()
        movie_Year = i.find("td",class_="titleColumn").span.get_text()
        movie_rating = i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        url = i.find("td",class_="titleColumn").a["href"]
        pos_num+=1
        movie_url = "https://www.imdb.com"+url
        movies_dic["Position"]=pos_num
        movies_dic["Movies_name"]=movie_title
        movies_dic["Movies_year"]=movie_Year
        movies_dic["Movie_rating"]=movie_rating
        movies_dic["Movie_url"]=movie_url
        movies_list.append(movies_dic.copy())
        with open("top250movies.json","w") as IMDB:
            json.dump(movies_list,IMDB,indent=4)
    return movies_list
scrape_top_list()


