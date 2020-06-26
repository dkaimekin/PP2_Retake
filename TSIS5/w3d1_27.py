import re


def splitter(string):
    spltd = re.split(r"\D+", string)
    for elem in spltd:
        print(elem)


print("Insert data:")
data = input()

splitter(data)
