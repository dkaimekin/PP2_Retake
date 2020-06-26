import re

print("Insert data:")
data = input()

pattern = re.compile(r'[\W_]+')
print(pattern.sub('', data))