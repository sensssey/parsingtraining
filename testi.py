import csv
import json

import requests
from bs4 import BeautifulSoup

Headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 "
                  "YaBrowser/24.4.0.0 Safari/537.36"
}
'''url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
req = requests.get(url)
src = req.text
with open("index.html", "w", encoding="utf-8") as file:
    file.write(src)
with open("index.html", encoding="UTF-8") as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml")
dict = {}
for i in soup.find_all(class_ = "mzr-tc-group-item-href"):
    dict[i.text] = "https://health-diet.ru" + i.get("href")

with open("dict.json", "w", encoding="utf-8") as file:
    json.dump(dict, file, indent=4, ensure_ascii=False)
'''
with open("dict.json", encoding="UTF-8") as file:
    all_categories = json.load(file)

count = 0

for i in all_categories:
    name = i
    href = all_categories[i]
    req = requests.get(url=href, headers=Headers)
    src = req.text
    with open(f"data/{count}_{name}.html", "w", encoding="UTF-8") as file:
        file.write(src)
    with open(f"data/{count}_{name}.html", encoding="UTF-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    try:
        table_head = soup.find(class_="uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed").find("tr").find_all("th")
        product = table_head[0].text
        calories = table_head[1].text
        proteins = table_head[2].text
        fats = table_head[3].text
        carbohydrates = table_head[4].text
        with open(f"data/{count}_{name}.csv", "w", encoding="UTF-8-sig") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(
                (product, calories, proteins,  fats, carbohydrates)
            )
        productinfo = []
        for i in soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr"):
            product_tds = i.find_all("td")
            title = product_tds[0].find("a").text
            calories = product_tds[1].text
            proteins = product_tds[2].text
            fats = product_tds[3].text
            carbohydrates = product_tds[4].text
            productinfo.append(
                {
                    "Title": title,
                    "Calories": calories,
                    "Proteins": proteins,
                    "Fats": fats,
                    "Carbohydrates": carbohydrates
                }
            )
            with open(f"data/{count}_{name}.csv", "a", encoding="UTF-8-sig") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    (title, calories, proteins, fats, carbohydrates)
                )
            with open(f"data/{count}_{name}.json", "w", encoding="UTF-8-sig") as file:
                json.dump(productinfo, file, indent=4, ensure_ascii=False)
    except:
        print("братан хуйня какая-то")
    count += 1



