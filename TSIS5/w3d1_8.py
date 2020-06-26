import re


def is_contain(string):
    patterns = '^[a-z]+_[a-z]+$'
    if not re.search(patterns, string):
        print("Match!")
    else:
        print("No match.")

data = input()
is_contain(data)
