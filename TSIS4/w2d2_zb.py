def beat(bishopF, figureF):
    if bishopF[0] > figureF[0]:         # Case when x of the bishop is greater than x of the figure
        if bishopF[1] > figureF[1]:     # Case when y of the bishop is greater than y of the figure
            cycles = bishopF[0] - figureF[0]
            for i in range(cycles):
                bishopF[0] -= 1
                bishopF[1] -= 1
                if bishopF[0] == figureF[0] and bishopF[1] == figureF[1]:
                    return True
                elif bishopF[0] == figureF[0] and bishopF[1] != figureF[1] \
                        or bishopF[0] != figureF[0] and bishopF[1] == figureF[1]:
                    return False
        elif bishopF[1] < figureF[1]:
            cycles = bishopF[0] - figureF[0]
            for i in range(cycles):
                bishopF[0] -= 1
                bishopF[1] += 1
                if bishopF[0] == figureF[0] and bishopF[1] == figureF[1]:
                    return True
                elif bishopF[0] == figureF[0] and bishopF[1] != figureF[1] \
                        or bishopF[0] != figureF[0] and bishopF[1] == figureF[1]:
                    return False

    elif bishopF[0] < figureF[0]:       # Case when x of the figure is greater than x of the bishop
        if bishopF[1] < figureF[1]:     # Case when y of the figure is greater than y of the bishop
            cycles = figureF[0] - bishopF[0]
            for i in range(cycles):
                bishopF[0] += 1
                bishopF[1] += 1
                if bishopF[0] == figureF[0] and bishopF[1] == figureF[1]:
                    return True
                elif bishopF[0] == figureF[0] and bishopF[1] != figureF[1] \
                        or bishopF[0] != figureF[0] and bishopF[1] == figureF[1]:
                    return False
        elif bishopF[1] > figureF[1]:
            cycles = figureF[0] - bishopF[0]
            for i in range(cycles):
                bishopF[0] += 1
                bishopF[1] -= 1
                if bishopF[0] == figureF[0] and bishopF[1] == figureF[1]:
                    return True
                elif bishopF[0] == figureF[0] and bishopF[1] != figureF[1] \
                        or bishopF[0] != figureF[0] and bishopF[1] == figureF[1]:
                    return False
    else:
        return False


bishop = []
figure = []
data = input()

if len(data) > 1:
    data = data.split(" ")

    bishop.append(int(data[0]))
    bishop.append(int(data[1]))

    figure.append(int(data[2]))
    figure.append(int(data[3]))

else:
    bishop.append(int(data))
    bishop.append(int(input()))
    figure.append(int(input()))
    figure.append(int(input()))

result = beat(bishop, figure)

if result:
    print("YES")
else:
    print("NO")

