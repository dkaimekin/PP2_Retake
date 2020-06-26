import re


def is_contain(string, words):
    for word in words:
        if re.search(word, string):
            print("Match!")
        else:
            print("No match.")


print("Insert text: \n")
data = input()

print("Insert words: \n")
search = input()
search = search.split(" ")

is_contain(data, search)
