import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
news = []
news_other = []

for item in root.findall(r'./channel/item'):
    date = item.findtext('pubDate')
    title = item.findtext('title')
    items_data = {}
    for item_data in item:
        items_data[item_data.tag] = item_data.text

    news.append({'pubDate': date, 'title': title})
    news_other.append(items_data)

with open('news.json', 'w', encoding='utf-8') as thread:
    json.dump(news, fp=thread, ensure_ascii=False, indent=4)
with open('news_other.json', 'w', encoding='utf-8') as thread:
    json.dump(news_other, fp=thread, ensure_ascii=False, indent=4, sort_keys=True)