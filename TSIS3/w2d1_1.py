def palindrome(s):
    return s == s[::-1]

s = input()
result = palindrome(s)
if result:
    print("YES")
else:
    print("NO")