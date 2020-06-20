def palindrome(number):
   if len(number) <= 1:
       return True
   if number[0] == number[len(number)-1]:
       return palindrome(number[1:len(number)-1])
   else:
       return False

amount = int(input())
for i in range(0, amount):
    number = input()
    if palindrome(number):
        print("Yes")
    else:
        print("No")

