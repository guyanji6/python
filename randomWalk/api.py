import requests
import pygal
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(r.status_code)
response_dict = r.json()
print(response_dict.keys() )
repo_dicts = response_dict['items']



names,stars =[],[]
for i in repo_dicts:
    names.append(i['name'])
    stars.append(i['stargazers_count'])
chart = pygal.Bar(x_label_rotation=45,c='red')
chart.title = 'stars'
chart.x_labels = names
chart.add('',stars)
chart.render_to_file('guthub stats.svg')
