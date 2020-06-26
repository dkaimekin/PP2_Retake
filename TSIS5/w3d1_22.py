import re


def find_position(text, word):
    pattern = word
    match = re.search(pattern, text)
    for match in re.finditer(pattern, text):
        start = match.start()
        end = match.end()
        print('{} occurred at {}:{} '.format(text[start:end], \
                                                        start, end))


print("Insert text:")
data = input()

print("Insert word:")
word = input()

find_position(data, word)
