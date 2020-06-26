import re


def p_finder(string):
    for s in string:
        match = re.match("(P\w+)\W(P\w+)", s)
        if match:
            print(match.groups())


strings = []
for i in range(1, 4):
    print("Insert a string ({}/3):".format(i))
    strings.append(input())

p_finder(strings)
