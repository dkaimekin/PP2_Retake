def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):

    divider = gcd(a, b)
    return a * b / divider

inpt = input()
inpt = inpt.split(" ")
x = int(inpt[0])
y = int(inpt[1])

greatest = gcd(x, y)
least = lcm(x, y)

result = int(greatest + least)

print(result)


