import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from task import scrape_top_list
from task5 import get_movie_list_details

def analyse_movies_gener():
    gener_list = []
    gener_dict = {}
    top_movies = scrape_top_list()
    gener_detail = get_movie_list_details(top_movies[:250])
    for i in gener_detail:
        D = i["gener"]
        if D not in gener_list:
            gener_list.append(D)
    for j in gener_list:
        gener_dict[j]=[]
        count = 0
        for d in gener_detail:
            dr = d["gener"]
            if dr==j:
                count+=1
        gener_dict[j].append(count)
    return gener_dict
pprint(analyse_movies_gener())