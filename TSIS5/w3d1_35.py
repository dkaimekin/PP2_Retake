import re

print("Insert data:")
data = input()

print(re.findall(r"\b\w{4,}\b", data))