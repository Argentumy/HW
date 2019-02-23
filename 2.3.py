import json
from pprint import pprint


with open('newsafr.json') as file:
    news = json.load(file)
    # pprint(news)
    # pprint(news['description'])
    # print(type(news))
    # pprint(news.values())

# Посчитать слова в новостях
# Отсортировать по частоте встречаемости
# Убрать все слова менее 6 символов

news2 = news.get("rss", {}).get("channel", {}).get("items", False)
string = []
string2 = []
string3 = []



for a in news2:
    string.append(a['description'].split(sep=' '))
# pprint(string)

for b in string:
    # print(b)
    for c in b:
        if len(c) >= 6:
            string2.append(c)
            # print(len(c))

string3 = string2.sort(key=len, reverse=True)
pprint(string2)

# pprint(len(string))
