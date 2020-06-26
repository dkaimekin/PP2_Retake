import re


def format_date(date):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)


print("Insert date(YYYY-MM-DD):")
data = input()

print(format_date(data))