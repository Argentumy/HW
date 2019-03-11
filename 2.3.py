# import json
# from pprint import pprint
# import collections
#
# with open('newsafr.json', encoding='utf-8') as file:
#     news = json.load(file)
#
# news2 = news.get("rss", {}).get("channel", {}).get("items", False)
# string = []
# string2 = []
# string3 = []
#
#
# def task(self):
#     for a in self:
#         string.append(a['description'].lower().split(sep=' '))
#
#     for b in string:
#         for c in b:
#             if len(c) >= 6:
#                 string2.append(c)
#
#     string2.sort(key=len, reverse=True)
#
#     return string2
#
#
# task(news2)
#
# string3 = collections.Counter(string2).most_common(10)
# pprint(string3)


# Task 2

import xml.etree.ElementTree as ET
import collections
from pprint import pprint


tree = ET.parse('newsafr.xml')
root = tree.getroot()
xml_title = root.findall('channel/item/description')

string = []
string2 = []


def task(self):
    for a in self:
        string.append(a.text.lower().split(sep=' '))

    for b in string:
        for c in b:
            if len(c) >= 6:
                string2.append(c)

    string2.sort(key=len, reverse=True)

    return string2


task(xml_title)


string3 = collections.Counter(string2).most_common(10)
pprint(string3)
