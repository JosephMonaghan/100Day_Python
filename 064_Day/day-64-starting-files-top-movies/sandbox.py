import json


with open("dump.json",'r') as file:
    data = json.load(file)



top_hit = data['results'][0]
print(top_hit.keys())

title = top_hit['title']
description = top_hit['overview']
year = int(top_hit['release_date'].split("-")[0])
rating = top_hit['vote_average']
url = f"https://image.tmdb.org/t/p/original/{top_hit['poster_path']}"

print(url)

# for key, value in top_hit:
#     print(f"{key}: {value}")