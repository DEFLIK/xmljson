from urllib.request import urlopen, quote
from json import loads
from itertools import groupby


url = "https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=" + quote('Бельмондо,_Жан-Поль')
data = loads(urlopen(url).read().decode('utf8'))
revisions = data['query']['pages']['192203']['revisions']
for k, g in groupby(revisions, lambda x: str.split(x['timestamp'], 'T')[0]):
    print(f'{k}, {len(list(g))}')

# 2021-09-06 числа встречено 58 правок. Дата связана со смертью
# Такой метрикой вряд ли можно пользоваться, т.к. он не является точной,
# но нельзя отрицать, что в некоторых случаях закономерность присутсвует 
