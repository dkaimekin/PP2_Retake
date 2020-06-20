matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
trans_matrix = list(matrix)


for i in range(0, 3):
    for j in range(0, 3):
        trans_matrix[i][j] = matrix[j][i]
print(matrix)
maxTop = []
maxLeft = []


for i in range(0, 3):
    largest = 0
    for j in range(0, 3):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
    maxTop.append(largest)
print(matrix)

for i in range(0, 3):
    largest = 0
    for j in range(0, 3):
        if trans_matrix[i][j] > largest:
            largest = trans_matrix[i][j]
    maxLeft.append(largest)

print(maxTop)
print(maxLeft)
print(trans_matrix)