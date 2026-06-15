import json

def load_context(path):

    with open(path,
              encoding="utf8") as f:

        docs = json.load(f)

    return docs