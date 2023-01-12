import json


def load_data(path):
    with open(path) as data:
        data = json.load(data)
        
    return data

