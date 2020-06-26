import re


def ae_finder(string):
    return re.findall(r"[ae]\w+", string)

print("Insert data:")
data = input()

print(ae_finder(data))