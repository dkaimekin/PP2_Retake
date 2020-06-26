import re


def camel_to_snake(string):
    snake_string = re.sub("(.)([A-Z][a-z]+)", r'\1_\2', string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake_string).lower()


print("Insert data:")
data = input()

print(camel_to_snake(data))