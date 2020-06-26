import re

def is_contain(string):
    patterns = '^[a-zA-z0-9_]*$'
    if re.search(patterns, string):
        print("Match!")
    else:
        print("No match.")

data = input()
is_contain(data)
