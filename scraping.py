import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import urllib3
import json


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
    indentCount = 0
    while (indentCount < 1):
        indentCount = int(input("Please input indent count:"))

    data = json.dumps(countSorted, indent = indentCount)
    print(data)

    return countSorted


    



pages = input("Please enter how many pages you want to check:")

try:
    int(pages)
except:
    raise TypeError("Please input valid page")

countSorted = quotaCount(pages)
