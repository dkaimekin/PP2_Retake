import re


def is_contain(string):
    char_re = re.compile(r'[^a-zA-z0-9.]')
    string = char_re.search(string)
    return not bool(string)


data = input()
print(is_contain(data))
