from urllib.request import urlopen
from urllib.error import HTTPError
import json


def get_definition(
    word,
):  # https://www.section.io/engineering-education/integrating-external-apis-with-flask/
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word)
    try:
        response = urlopen(url)
    except HTTPError:
        return "Word not found!"
    data = response.read()
    word_dict = json.loads(data)
    return clean_definition(word_dict)


def clean_definition(word_dict):
    definition_str = ""
    definitions = word_dict[0]["meanings"][0]["definitions"]
    for idx, def_dict in enumerate(definitions):
        def_str = def_dict["definition"]
        definition_str += f"{idx+1}) {def_str}\n"
    return definition_str


if __name__ == "__main__":
    word = "moon"
    definition = get_definition(word)
    print(definition)
