import re

print("Insert data:")
data = input()

print(re.findall('[A-Z][^A-Z]*', data))