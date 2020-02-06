import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        x = input("Did you mean %s instead? Type 'Y' if yes, type 'N' if no: " % get_close_matches(w, data.keys())[0])
        if x == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif x == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter words: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
