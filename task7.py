import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from task import scrape_top_list
from task5 import get_movie_list_details

def analyse_movies_directors():
    director_list = []
    director_dict = {}
    top_movies = scrape_top_list()
    director_detail_list = get_movie_list_details(top_movies[:250])
    for i in director_detail_list:
        D = i["movie_dirctor_name"]
        if D not in director_list:
            director_list.append(D)
    for j in director_list:
        director_dict[j]=[]
        count = 0
        for d in director_detail_list:
            dr = d["movie_dirctor_name"]
            if dr==j:
                count+=1
        director_dict[j].append(count)
        with open ("movies directors.json","w")as IMDB:
            json.dump(director_dict,IMDB,indent=2)
    return director_dict
pprint(analyse_movies_directors())