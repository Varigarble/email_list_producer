n = int(input("Enter an integer to convert to binary: "))

out = []
bit_exp = 0
i = -1

while n / 2 ** bit_exp >= 1:
    if ((n // 2 ** bit_exp) % 2) == 0:
        out.insert(i, 0)
    else:
        out.insert(i, 1)
    bit_exp += 1
    i -= 1

print(''.join(str(x) for x in out))

'''Varigarble -- 2020'''
