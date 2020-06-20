gems = int(input())
remains = gems

for i in range(1, gems + 2):
    bob = i
    nelson = 2*i
    remains -= bob
    if remains <= 0:
        print("Bob")
        break
    remains -= nelson
    if remains <= 0:
        print("Nelson")
        break