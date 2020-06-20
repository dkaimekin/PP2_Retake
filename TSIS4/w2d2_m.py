def percentage(numbers):
    result = []
    odd = 0
    even = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    if odd == 0:
        result.append(0)
        result.append(100)
    elif even == 0:
        result.append(100)
        result.append(0)
    else:
        result.append(odd / len(numbers) * 100)
        result.append(even / len(numbers) * 100)
    return result


val = True
dataInt = []
while val:
    data = input()
    data = data.split(" ")
    for i in range(len(data)):
        if "-" in data[i]:
            val = False
            break
        dataInt.append(int(data[i]))


output = percentage(dataInt)
if output[0] - int(output[0]) == 0:
    print("{}% {}%".format(int(output[1]), int(output[0])))
else:
    print("{:.4f}% {:.4f}%".format(output[1], output[0]))