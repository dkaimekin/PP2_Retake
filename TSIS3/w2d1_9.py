matrix1 = []
matrix2 = []
matrix3 = []

n = int(input())

for i in range(0, n):
    row = []
    rowString = input()
    rowString = rowString.split(" ")
    for j in range(0, n):
        rowInt = int(rowString[j])
        row.append(rowInt)
    matrix1.append(row)

x = input()

for i in range(0, n):
    row = []
    rowString = input()
    rowString = rowString.split(" ")
    for j in range(0, n):
        rowInt = int(rowString[j])
        row.append(rowInt)
    matrix2.append(row)

for i in range(0, n):
    row = []
    for j in range(0, n):
        piece = 0
        for a in range(0, n):
            elem = matrix1[j][a] * matrix2[a][j]
            piece += elem
        row.append(piece)
    matrix3.append(row)


for i in range(0, n):
    output = ""
    for j in range(0, n):
        char = str(matrix3[i][j])
        output = output + char + ' '
    print(output)




