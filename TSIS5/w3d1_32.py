import re

print("Insert data:")
data = input()

print(re.sub("[ .,]", ':', data, 2))