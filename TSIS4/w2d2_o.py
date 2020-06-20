def how_many(pillar, scale):
    number = 0
    maximum = 0
    for i in range(scale[0], scale[1] + 1):
        if pillar[i] > maximum:
            maximum = pillar[i]
            number += 1
    return number


amount = int(input())
pillarHeight = []

pillars = input()
pillars = pillars.split(" ")
for i in range(amount):
    pillarHeight.append(int(pillars[i]))

cycles = int(input())
for i in range(cycles):
    scaleInt = []
    scale = input()
    scale = scale.split(" ")
    scaleInt.append(int(scale[0]))
    scaleInt.append(int(scale[1]))

    result = how_many(pillarHeight, scaleInt)
    print(result)