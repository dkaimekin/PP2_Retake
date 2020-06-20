def chess_matrix(x, y):
    matrix = []

    for i in range(0, y):
        if i % 2 == 0:
            row = []
            for j in range(0, x):
                if j % 2 == 0:
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)

        else:
            row = []
            for j in range(0, x):
                if j % 2 == 0:
                    row.append(0)
                else:
                    row.append(1)
            matrix.append(row)

    for i in range(0, y):
        for j in range(0, x):
            matrix[i][j] = str(matrix[i][j])
    return matrix


data = input()
data = data.split(" ")
y = int(data[0])
x = int(data[1])

result = chess_matrix(x, y)


for i in range(0, y):
    output = ""
    for j in range(0, x):
        output += result[i][j]
    print(output)

