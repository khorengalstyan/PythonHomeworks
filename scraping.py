import requests
from bs4 import BeautifulSoup
from collections import defaultdict



def quotaCount(pages):
    url = 'https://quotes.toscrape.com/page/'
    count = defaultdict(int)
    for page in range(1, pages):
        urlPage = url + str(page)
        resp = requests.get(urlPage)

        if (resp.status_code == 200):
            soup = BeautifulSoup(resp.text, 'html.parser')
            tags = soup.find_all(class_='tag')
            for tag in tags:
                name = tag.getText()
                count[name] += 1
        else:
            print("Error:")
    countSorted = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    return countSorted

def toJson(countSorted):
    for toJson in countSorted:
        print("{\n", "     ", "\"", toJson, "\":" , " ", "\"",countSorted.get(toJson),"\"\n}")

pages = 10
countSorted = quotaCount(pages)
toJson(countSorted)