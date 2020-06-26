import re


def extract_date(text):
    return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', text)


# test url:
# https://www.telegraph.co.uk/news/2020/06/26/glasgow-stabbing-armed-police-reportedly-seen-storming-hotel/
print("Insert URL:")
data = input()

print(extract_date(data))
