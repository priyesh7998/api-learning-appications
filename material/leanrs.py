from pathlib import Path
import json

FILE_DIR = Path("material")
FILE_PATH = FILE_DIR / "learns.txt"

def learns_file():
    with open(FILE_PATH, "a") as f:
        content = f.write("Function\n, List & Dict\n, File handling\n, JSON, Exceptions\n, Module & Packages\n")
        json.dump(content, f, indent=2)
        print(content)



def make_directory():
    FILE_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Directory '{FILE_DIR}' created successfully.")


make_directory()
learns_file()


  