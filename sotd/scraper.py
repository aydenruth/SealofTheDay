from bs4 import BeautifulSoup
import requests

def getSeal():
    goo = requests.get("https://www.reddit.com/r/seals/").text.replace("amp;", '')

    soup = BeautifulSoup(goo, 'lxml')
    imgs = soup.find('img')
    imgs = imgs['src']
    #element atributes r a dict, once u find ur el just access as normal
    multiImgs = soup.find('img', class_ = 'media-lightbox-img h-full w-full max-h-[100vw] object-contain mb-0 relative')
    #if u wanted to get all the imgs of each tag on a page use soup.find_all
    return imgs
    

