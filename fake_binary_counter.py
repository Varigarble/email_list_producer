init = [0, 0, 0, 0, 0]
end = [list(init)]
i = len(init) - 1

while i >= 0:
    if init[i] == 0:
        init[i] = 1
        init = init[0:i+1] + [0 for x in range(len(init[i:])-1)]
        end.append(list(init))
        i = len(init) - 1
    elif init[i] == 1:
        i -= 1

for binnum in end:
    print(end.index(binnum), binnum)

'''Varigarble -- 2020'''
