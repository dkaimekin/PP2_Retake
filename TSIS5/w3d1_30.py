import re

print("Insert address:")
address = input()

print(re.sub('Road$', 'Rd.', address))