import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import urllib3


urllib3.disable_warnings()


def quotaCount(pages):
    url = 'https://quotes.toscrape.com/page/'
    count = defaultdict(int)
    for page in range(1, int(pages)):
        urlPage = url + str(page)
        response = requests.get(urlPage, verify=False)

        if (response.status_code == 200):
            soup = BeautifulSoup(response.text, 'html.parser')
            tags = soup.find_all(class_='tag')
            for tag in tags:
                name = tag.getText()
                count[name] += 1
        else:
            print("Error: Something went wrong")
    countSorted = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    return countSorted

def toJson(countSorted):
    for toJson in countSorted:
        print("{\n", "     ", "\"", toJson, "\":" , " ", "\"",countSorted.get(toJson),"\"\n}")


pages = input("Please enter how many pages you want to check:")

try:
    int(pages)
except:
    raise TypeError("Please input valid page")

countSorted = quotaCount(pages)
toJson(countSorted)
