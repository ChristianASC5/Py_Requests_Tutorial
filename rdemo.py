import requests

r = requests.get("https://imgs.xkcd.com/comics/into_my_veins.png")

with open('comic.png', 'wb') as f:
    f.write(r.content)
