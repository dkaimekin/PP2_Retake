data = input()
letters = []

for i in range(0, len(data)):
    if data[i] not in letters:
        letters.append(data[i])

s = ""
for i in range(0, len(letters)):
    s += letters[i]

print(s)