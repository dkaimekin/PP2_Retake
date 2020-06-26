import re


print("Insert data:")
data = input()

print(re.sub(r'\s+', '', data))