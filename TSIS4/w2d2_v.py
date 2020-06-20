amount = int(input())
time = []

for i in range(amount):
    numbers = input()
    numbers = numbers.split(" ")
    row = []
    for j in range(3):
        row.append(int(numbers[j]))
    time.append(row)


for a in range(len(time) - 1):
    for i in range(len(time) - 1):
        if time[i][0] > time[i + 1][0]:
            time[i], time[i + 1] = time[i + 1], time[i]
        elif time[i][0] == time[i+1][0]:
            if time[i][1] > time[i+1][1]:
                time[i], time[i + 1] = time[i + 1], time[i]
            elif time[i][1] == time[i+1][1]:
                if time[i][2] > time[i+1][2]:
                    time[i], time[i + 1] = time[i + 1], time[i]

for i in range(len(time)):
    output = ""
    for j in range(3):
        output += str(time[i][j]) + " "
    print(output)

