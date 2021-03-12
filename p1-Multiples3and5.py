#Nathan Li - 3/10/2021 - P1: Multiples of 3 and 5

multiplesBelow1000 = []

for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        multiplesBelow1000.append(x)

finalSum = sum(multiplesBelow1000)
print(finalSum)