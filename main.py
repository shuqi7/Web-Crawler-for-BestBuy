import requests
from bs4 import BeautifulSoup

def webCrawler(maxPages):
    page = 1
    while page <= maxPages:
        url = "https://www.bestbuy.ca/en-ca/category/led-monitors/474833.aspx?type=product&page=" + str(page)
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        soupObject = BeautifulSoup(plainText, "html.parser")
        for content in soupObject.findAll('div',{'class':'prod-info'}):
            price = content.find('span',{'class':'amount'}).string
            prodTitle = content.find('h4',{'class':'prod-title'}).string
            print(prodTitle + ": " + price)
        page += 1;


webCrawler(19)