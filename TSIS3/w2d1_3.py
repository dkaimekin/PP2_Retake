number = input()
number = number.split(" ")


l = int(number[0])
r = int(number[1])
output = ""
for i in range(l, r + 1):
    if i % 7 == 1 or i % 7 == 2 or i % 7 == 5:
        i = str(i)
        output = output + i + " "
print(output)