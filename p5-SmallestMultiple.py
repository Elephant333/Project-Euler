#Nathan Li - 3/10/2021 - P5: Smallest Multiple

num = 20
divideBy = range(1,21)
found = False
while found == False:
    for x in divideBy:
        if num % x == 0:
            pass
        else:
            num += 20
            break
    else:
        found = True

print(num)