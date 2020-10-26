n = input("Enter a binary number to convert to decimal: ")

bit_exp = 0
decimals = []

for bit in n[::-1]:
    if int(bit) == 1:
        decimals.append(2**bit_exp)
    bit_exp += 1

decimal = sum(decimals)
print(decimals)
print(decimal)

'''Varigarble -- 2020'''
