clients = int(input())
client_height = []

data = input()
data = data.split(" ")
for i in range(0, clients):
    client_height.append(int(data[i]))

limit = int(input())

amount = 0
for i in range(0, clients):
    if client_height[i] >= limit:
        amount += 1

print(amount)