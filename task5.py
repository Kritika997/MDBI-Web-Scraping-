import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from task import scrape_top_list

movie_list_10 = []
movie_detail = {}
def get_movie_list_details(details):
    top_movies = details[:250]
    for i in top_movies:
        name = i["Movies_name"]
        url = i["Movie_url"]
        get_url = requests.get(url)
        soup = BeautifulSoup(get_url.text,"html.parser")
        title = soup.find("div",class_="title_wrapper").h1.get_text()
        lang = soup.find("div",class_="article",id="titleDetails")
        divs_tags = lang.find_all("div")
        for i in divs_tags:
            h4_tag = i.find_all('h4')
            for j in h4_tag:
                if "Language:" in j:
                    a_tag= i.find_all('a')
                    for language in a_tag:
                        movie_language = language.get_text()
        time_hours = soup.find("div",class_="subtext").time.get_text().strip()
        minutes = int(time_hours[0])*60
        gener = soup.find("div",class_="subtext").a.get_text().strip()
        bio = soup.find("div",class_="plot_summary").div.get_text().strip()
        director = soup.find("div",class_="credit_summary_item").a.get_text().strip()
        movie_poster_link = soup.find("div",class_="poster").a["href"]
        final_poster_link = "https://www.imdb.com"+movie_poster_link
        movie_detail["movie_title"]=title
        movie_detail["Language"]=movie_language
        movie_detail["Country"]="India"
        movie_detail["movie_timig"]=minutes
        movie_detail["gener"]=gener
        movie_detail["movie_bio"]=bio
        movie_detail["movie_dirctor_name"]=director
        movie_detail["poster_link"]=final_poster_link
        movie_list_10.append(movie_detail.copy())
        with open ("250moviesdata.json","w") as IMDB:
            json.dump(movie_list_10,IMDB,indent=4)
    return movie_list_10
get_movie_list_details(scrape_top_list())