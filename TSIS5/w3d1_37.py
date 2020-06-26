import re


def snake_to_camel(string):
    for word in string.split('_'):
        result = ''.join(word.capitalize())