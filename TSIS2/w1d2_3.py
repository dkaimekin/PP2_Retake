bits = []
a = int(input())

def dec_to_bin(a):
    if a > 1:
        dec_to_bin(a // 2)
        bits.append(a % 2)
    else:
        bits.append(a)

dec_to_bin(a)
bits.reverse()
rev_num = 0
power = 3
for i in bits:
    rev_num += (i * 2**power)
    power -= 1

print(rev_num)