import re

def is_contain(string):
    text = re.sub('\.[0]*', '.', string)
    return text


data = input()
print(is_contain(data))