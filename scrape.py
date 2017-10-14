import urllib
import json
import requests
from bs4 import BeautifulSoup
import csv

pageNum = 71
pitchforkUrl = "https://pitchfork.com/"
my_list = []

def artist(soup):
    name = soup.find("h2",{"class":"artists"})
    artist = []
    for li in name.findAll('a'):
        artist.append(li.string.encode('utf-8'))
    return(''.join(map(str, artist)))

def rate(soup):
    rating = soup.find("span", {"class":"score"}).string
    return float(rating)

def albumName(soup):
    name = soup.find("h1",{"class":"review-title"}).string.encode('utf-8')
    return(name)

def bnm(soup): # boolean to determine if it has a best new music tag
    bnm = soup.find("p",{"class":"bnm-txt"})
    if bnm is None:
        return 0
    else:
        return 1

def genre(soup):
    for ul in soup.find_all('ul', class_='genre-list'):
        type = ul.a.string.encode('utf-8') 
        return(type)

def pubDate(soup):
    date = soup.find('time', {'class':'pub-date'}).string.encode('utf-8')
    return(date)

def abstract(soup): # short summary of album before actual review
    desc = soup.find('div', {'class':'abstract'}).text.encode('utf-8').rstrip()
    return(desc)

def fullDesc(soup):
    desc = soup.find('div', {'class':'clearfix'})
    detail = desc.find('div', {'class':'contents'})
    paragraph = []
    VALID_TAGS = ['div', 'p']
    for para in detail.findAll('p'):
        if para.name not in VALID_TAGS:
            para.replaceWith(para.renderContents())
        paragraph.append(para.get_text().encode('utf-8'))
    return(' '.join(map(str, paragraph)))
  
    
def initializeSoup(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    return soup

def review(url): #gets all metadata from each album review and puts it into a list
    fullUrl = "https://pitchfork.com/" + url
    soup = initializeSoup(fullUrl)
    
    lst = []
    lst.append(artist(soup))
    lst.append(rate(soup))
    lst.append(albumName(soup))
    lst.append(bnm(soup))
    lst.append(genre(soup))
    lst.append(pubDate(soup))
    lst.append(abstract(soup))
    lst.append(fullDesc(soup))
    print(lst)
    
    my_list.append(lst)


# iterates through every page of 'Reviews' and finds URLs
while (pageNum < 81):
    website = "https://pitchfork.com/reviews/albums/?page=" + str(pageNum)
    soup = initializeSoup(website)

    albums = soup.find("div", {"class":"review-collection-fragment"})
    albumLinks = albums.find_all("div", {"class":"review"})

    for albumLink in albumLinks:
        link = albumLink.find("a", {"class":"album-link"})
        url = link.get("href")
        review(url)
        
    pageNum+=1

# write to csv
with open("output71-80.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerows(my_list)
        
