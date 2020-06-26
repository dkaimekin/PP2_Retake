import re


def is_contain(string):
    patterns = 'a.*?b$'
    if re.search(patterns, string):
        print("Match!")
    else:
        print("No match.")

data = input()
is_contain(data)
