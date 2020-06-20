matrix = []
matrixTrans = []
n = int(input())

for i in range(0, n):
    row = []
    data = input()
    data = data.split(" ")
    for j in range(0, n):
        row.append(int(data[j]))
    matrix.append(row)

for i in range(0, n):
    row = []
    for j in range(0, n):
        row.append(matrix[j][i])
    matrixTrans.append(row)

leftMax = []
for i in range(0, n):
    largest = 0
    for j in range(0, n):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
    leftMax.append(largest)

topMax = []
for i in range(0, n):
    biggest = 0
    for j in range(0, n):
        if matrixTrans[i][j] > biggest:
            biggest = matrixTrans[i][j]
    topMax.append(biggest)

leftArea = 0
for i in range(0, n):
    leftArea += leftMax[i]

topArea = 0
for i in range(0, n):
    topArea += topMax[i]

floorArea = 0
for i in range(0, n):
    for j in range(0, n):
        if matrix[i][j] != 0:
            floorArea += 1

print(leftArea + topArea + floorArea)