import requests

URL = "https://jsonplaceholder.typicode.com/posts/"
try:
    resonse = requests.get(URL)
    data = resonse.json()
    for dat in data:
        print(f"Title: {dat["title"]}\nBODY: {dat["body"]}")
except Exception as e:
    print(f"ERROR MESSAGE: {e}")