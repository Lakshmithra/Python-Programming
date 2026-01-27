import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"

data = requests.get(url)
if data.status_code != 200:
    print("Error ! Webdata can't be retrieved")
else:
    soup = BeautifulSoup(data.content , "xml")
    headlines = soup.find_all("item")
    print("HEADLINES :-\n")
    for i,j in enumerate(headlines , start = 1):
        print(i ,"-" , j.title.text)
