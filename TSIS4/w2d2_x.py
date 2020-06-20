def converter(number, base):
    output_f = ""
    if number == 0:
        return 0
    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    number_out = digits[::-1]
    for i in range(0, len(number_out)):
        number_out[i] = str(number_out[i])
        output_f += number_out[i]
    return output_f


data = int(input())

output = converter(data, 7)
print(output)