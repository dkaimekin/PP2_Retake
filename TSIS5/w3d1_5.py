import re


def is_contain(string):
    patterns = 'abbb+?'
    if re.search(patterns, string):
        print("Match!")
    else:
        print("No match.")

data = input()
is_contain(data)
