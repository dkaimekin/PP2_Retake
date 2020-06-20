s = input()
t = input()


def isAnagram(s,t):
    sSorted = sorted(s)
    tSorted = sorted(t)

    if sSorted == tSorted:
        print("Yes")
    else:
        print("No")


isAnagram(s,t)