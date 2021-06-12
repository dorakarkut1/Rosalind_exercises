
AAAA = 1
AAAa = 1
AAaa = 1
AaAa = 3/4
Aaaa = 1/2

numbers = [16364, 17794, 17756, 17699, 19952, 16857]
all = (AAAA * numbers[0] + AAAa*numbers[1] + AAaa*numbers[2] + AaAa*numbers[3] + Aaaa*numbers[4])*2
print(all)