def checker(s, len1, len2):
    yes = True
    for i in range(0, len1):
        if "0" <= s[i] <= "9":
            pass
        else:
            yes = False
    if s[len1] == "-":
        pass
    else:
        return False
    for i in range(len1 + 1, len1 + len2 + 1):
        if "0" <= s[i] <= "9":
            pass
        else:
            yes = False
    return yes


len = input()
len = len.split(" ")
len[0] = int(len[0])
len[1] = int(len[1])
code = input()

result = checker(code, len[0], len[1])

if result:
    print("Yes")
else:
    print("No")
