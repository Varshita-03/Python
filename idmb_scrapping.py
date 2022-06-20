#idmb web scrapping
#https://www.dropbox.com/s/0j39mqvboa2ny3a/links.csv

from bs4 import BeautifulSoup
import pandas as pd
import json 
import requests
 
def scrape_movie_index_page(movie_id):
    url="https://www.imdb.com/title/tt{}/". format(str(movie_id).zfill(7))
    current_page=requests.get(url)
    index_soup=BeautifulSoup(current_page.text,"html.parser")#converts into html
    current_page_json=index_soup.find("script",attrs={"type": "application/ld+json"})
    current_page_json=str(current_page_json)[str(current_page_json).find("{"):-9]
    return current_page_json
    

def collect_movie_data(movie_id=30):
    page_json=json.loads(scrape_movie_index_page(movie_id)) #json returns dictionary
    movie={
        "name": page_json["name"],
        "genre": page_json["genre"],
        "image": page_json["image"],
        "description": page_json["description"]
        }                             #movie is a dictionary
    print(movie["name"])
    return movie
    

def get_movie_id(num=30,page=1): #page no.from which we extract data
    links_data=pd.read_csv("links.csv")
    movie_data=list(links_data.imdbId)
    start_index=(page-1)*num
    end_index=start_index+num
    return movie_data[start_index:end_index]


#reading file usinf pd

#df=pd.read_csv("links.csv")
#print(type(df))
#print(df.head(30))  

#default 5
#data extraction using movie id

id=get_movie_id(10) #default num=30
for num in id:
    collect_movie_data(num)

