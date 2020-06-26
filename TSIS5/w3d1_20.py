import re


def find_position(text, word):
    pattern = word
    match = re.search(pattern, text)
    start = match.start()
    end = match.end()
    print('{} occurred in {} from {} to {} '.format(match.re.pattern, match.string, start, end))


print("Insert text:")
data = input()

print("Insert word:")
word = input()

find_position(data, word)
