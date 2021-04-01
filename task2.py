import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from task import scrape_top_list
All_movies_data = scrape_top_list()
year_list = []
year_dict1={}
def group_by_year(movies):
    for i in movies:
        Year = i["Movies_year"]
        if Year not in year_list:
            year_list.append(Year)
    for i in year_list:
        year_list.sort()
        year_dict1[i]=[]
    for i in movies:
        year = i["Movies_year"]
        for j in year_dict1:
            if year == j:
                year_dict1[j].append(i)
    with open("Movies_year_wise.json","w") as IMDB:
        json.dump(year_dict1,IMDB,indent=4)
    return year_dict1
movies_year_wise=group_by_year(All_movies_data)
