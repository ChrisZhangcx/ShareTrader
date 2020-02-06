import json


def json_reader(file: str):
    return json.load(open(file, "r", encoding="utf-8"))
