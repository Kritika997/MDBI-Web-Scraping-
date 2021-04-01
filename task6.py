import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from task import scrape_top_list
from task5 import get_movie_list_details

def analyse_movies_language():
    lan_list = []
    lan_dict = {}
    top_movies = scrape_top_list()
    movies_detail_list = get_movie_list_details(top_movies[:250])
    for i in movies_detail_list:
        l = i["Language"]
        if l not in lan_list:
            lan_list.append(l)
    lan_list.sort()
    for j in lan_list:
        lan_dict[j]=[]
        count = 0
        for k in movies_detail_list:
            a = k["Language"]
            if a==j:
                count+=1
        lan_dict[j].append(count) 
    with open ("movies language.json","w")as IMDB:
        json.dump(lan_dict,IMDB,indent=2)
    return lan_dict
pprint(analyse_movies_language())   
