import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from task import scrape_top_list
All_movies_data = scrape_top_list()

def group_by_decade(movies):
    dec_list = []
    dec_dict = {}
    for i in movies:
        y = int(i["Movies_year"][1:5])
        module = y%10
        dec = y-module
        if dec not in dec_list:
            dec_list.append(dec)
    dec_list.sort()
    for i in dec_list:
        dec_dict[i]=[]
    for j in dec_dict:
        a = j+9
        for k in movies:
            b = int(k["Movies_year"][1:5])
            if b<=a and b>=j:
                dec_dict[j].append(k)
    with open ("decades_movies.json","w")as IMDB:
        json.dump(dec_dict,IMDB,indent=4) 
    return dec_dict
group_by_decade(All_movies_data)