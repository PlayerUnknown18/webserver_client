import json


def open_as_json(path):
    with open(path,"r") as fin:
        json_data = json.loads(fin.read())
        print(json_data["packets"][0])

open_as_json("playlist_4.jsonc")
