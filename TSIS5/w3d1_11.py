import re


def is_contain(string):
    patterns = '\w+\S*$'
    if re.search(patterns, string):
        print("Match!")
    else:
        print("No match.")

data = input()
is_contain(data)
