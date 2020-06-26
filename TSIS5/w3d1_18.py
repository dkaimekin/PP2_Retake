import re


def is_contain(string):
    text = re.compile(r'[0-9]{1,3}')
    matches = text.finditer(string)

    for match in matches:
        print(match.group(0))


data = input()
is_contain(data)
