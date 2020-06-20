training = []

fence = input()
fence = fence.split(" ")
fence[0] = int(fence[0])
fence[1] = int(fence[1])

for i in range(0, fence[0]):
    row = []
    rowString = input()
    rowString = rowString.split(" ")
    for j in range(0, 3):
        rowInt = int(rowString[j])
        row.append(rowInt)
    training.append(row)



climb = False
for i in range(0, fence[0]):
    average = 0
    for j in range(0, 3):
        average += training[i][j]
    average = average / 3
    if average >= fence[1]:
        climb = True
        pass
    pass


if climb:
    print("YES")
else:
    print("NO")