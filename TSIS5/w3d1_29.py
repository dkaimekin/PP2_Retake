import re


def number_position(string):
    for match in re.finditer(r"\d+", string):
        print(match.group(0))
        print("Index position:", match.start())


print("Insert data:")
data = input()

number_position(data)