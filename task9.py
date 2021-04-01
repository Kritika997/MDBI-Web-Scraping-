import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import os,random,time
from task import get_movie_list_details

movie_detail={}
All_movies_data=scrape_top_list()
def scrape_movie_details():
    random_sleep = random.randint(1,3)
    movie_id = " "
    for i in url[27:]:
        if "/" not in i:
            movie_id+=i
        else:
            break
    file_name = movie_id
    if os.path.exists(file_name+".json"):
        F=open(file_name+".json")
        t = F.read()
        print("Great, you already have file in your laptop.Please check it..")
        return t
    else:
        time.sleep(random_sleep)
        print("Wait for a while i will get data from website to you:-)")
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
        movie_detail["movie_timig"]=minutes
        movie_detail["gener"]=gener
        movie_detail["movie_bio"]=bio
        movie_detail["movie_dirctor_name"]=director
        movie_detail["poster_link"]=final_poster_link
        with open(file_name+".json","w") as my_file:
            json.dump(movie_detail,my_file,indent=4)
        return movie_detail
pprint(scrape_movie_details())