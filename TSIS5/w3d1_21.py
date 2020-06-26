import re


def find_position(text, word):
    pattern = word
    for match in re.findall(pattern, text):
        print("Found {}".format(match))


print("Insert text:")
data = input()

print("Insert word:")
word = input()

find_position(data, word)
