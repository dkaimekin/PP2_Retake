import re


def is_contain(string):
    text = re.compile(r"^5")
    if text.match(string):
        print("Match!")
    else:
        print("No match.")


data = input()
is_contain(data)
