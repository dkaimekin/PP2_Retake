
def isBackHome(moves):
    upcnt = 0
    downcnt = 0
    leftcnt = 0
    rightcnt = 0
    for i in range(0, len(moves)):
        if moves[i] == "U":
            upcnt += 1
        elif moves[i] == "D":
            downcnt += 1
        elif moves[i] == "L":
            leftcnt += 1
        elif moves[i] == "R":
            rightcnt += 1
    if upcnt == downcnt and leftcnt == rightcnt:
        return True
    else:
        return False

move = []
data = input()
for i in range(0, len(data)):
    move.append(data[i])

output = isBackHome(move)
if output:
    print("True")
else:
    print("False")
