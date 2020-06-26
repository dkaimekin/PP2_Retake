import re

print("Insert data:")
data = input()

print(re.findall(r'"(.*?)"', data))