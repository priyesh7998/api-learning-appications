import requests
import os
import json
from pathlib import Path

URL = "https://pokeapi.co/api/v2/pokemon"

resopnse = requests.get(URL,timeout=10)
data = resopnse.json()

FILE_DIR = Path("pokemon-data")
FILE_PATH = FILE_DIR / "data.txt"

FILE_DIR.mkdir(parents=True, exist_ok=True)

def write_data():
    with open(FILE_PATH, "a") as f:
        content = data
        json.dump(data, f, indent=2)
        print("DATA WRITTEN SUCCESSFULLY!!!")
        #print(content)


write_data()

