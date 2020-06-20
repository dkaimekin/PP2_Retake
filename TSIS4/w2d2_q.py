data = int(input())

digits = [int(x) for x in str(data)]

count = 0
for i in range(len(digits)):
    count += digits[i]

if count % digits[len(digits) - 1] == 0:
    print("Yes")
else:
    print("No")
