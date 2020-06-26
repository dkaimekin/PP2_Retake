import re

print("Insert data:")
data = input()

print(re.findall(r"\b\w{3,5}\b", data))