import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from task import scrape_top_list
from task5 import get_movie_list_details
def analyse_language_and_directors():
    lan_list = []
    dic_list = []
    dir_lan_dict = {}
    top_movies = scrape_top_list()
    movies_detail_list = get_movie_list_details(top_movies[:250])
    for i in movies_detail_list:
        l = i["movie_dirctor_name"]
        if l not in dic_list:
            dic_list.append(l)
    for j in director_list:
        dic_lan_dict[j]=[]
    return dic_lan_dict
    #     for k in movies_detail_list:
    #         print("komal")
    #         lan1 = i["Language"]
    #         if lan1 not in lan_list:
    #             lan_list.append(lan)
    #     for l in lan_list:
    #         print("komal")
    #         dir_lan_dict[l]=[]
            # count = 0
            # for n in movies_detail_list:
            #     lan2 = n["Language"]
            #     if a==l:
            #         count+=1
            # dir_lan_dict[l].append(count)
print(analyse_language_and_directors())