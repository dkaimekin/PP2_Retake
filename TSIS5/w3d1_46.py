import re

print("Insert data:")
data = input()

for match in re.finditer(r'\w+ly', data):
    print('{}-{}: {}'.format(match.start(), match.end(), match.group(0)))