import requests
import plotly.express as px

# u = 'https://api.github.com/search/repositories?q=language:python+sort:stars'

# res = requests.get(u)
# d = res.json()

import json
from matplotlib import pyplot as plt
names, stars = [],[]

with open('d.json','r', encoding = 'utf-8' ) as f:
    res= json.load(f)
    # print(len(res['itmes']), type(res['items']))
    for item in res['items']:
        names.append(item['name'])
        stars.append(item['stargazers_count'])
        

plt.bar(names.stars)
plt.xticks(rotation = 45)




# print(type(data['items']))

# for items in res['items']:
    # print(type(item))