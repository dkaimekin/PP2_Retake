def point_check(numbers):
    x1 = numbers[0]
    y1 = numbers[1]
    x2 = numbers[2]
    y2 = numbers[3]
    x_pos = numbers[4]
    y_pos = numbers[5]

    x = False
    y = False
    if x1 > x2:
        if x_pos in range(x2, x1 + 1):
            x = True
    if x2 > x1:
        if x_pos in range(x1, x2 + 1):
            x = True
    if y1 > y2:
        if y_pos in range(y2, y1 + 1):
            y = True
    if y2 > y1:
        if y_pos in range(y1, y2 + 1):
            y = True

    if x and y:
        return True
    else:
        return False


data = input()
data = data.split(" ")
dataInt = []
for i in range(0, 6):
    dataInt.append(int(data[i]))

#print(dataInt)
result = point_check(dataInt)
if result:
    print("yes")
else:
    print("no")
