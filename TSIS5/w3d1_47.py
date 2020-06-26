import re

print("Insert data:")
data = input()

print(re.split(r';|,|\*| \n', data))