import urllib
import json
import requests
from bs4 import BeautifulSoup

pageNum = 1
pitchforkUrl = "https://pitchfork.com/"

def initializeSoup(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    return soup

while (pageNum < 2):
    website = "https://pitchfork.com/reviews/albums/?page=" + str(pageNum)
    soup = initializeSoup(website)

    albums = soup.find("div", {"class":"review-collection-fragment"})
    albumLinks = albums.find_all("div", {"class":"review"})

    for albumLink in albumLinks:
        link = albumLink.find("a", {"class":"album-link"})
        url = link.get("href")
        print(url)

    pageNum+=1
        
