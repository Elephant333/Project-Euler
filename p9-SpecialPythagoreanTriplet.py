#Nathan Li - 3/11/2021 - P9: Special Pythagorean Triplet

import time
startTime = time.time()

flag = False
"""for a in range(1,999):
    for b in range(a, 1000):
        for c in range(b,1001):
            if a**2 + b**2 == c**2:
                if a+b+c == 1000:
                    print(a*b*c)
                    flag = True
                    break
        if flag:
            break
    if flag:
        break"""
#The above method was very slow, took 49.43 seconds, so I gave it a second try below

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000-a-b #Problem says that sum of abc must by 1000, so we can avoid doing a third for loop by setting c equal to 1000-a-b
        if a**2 + b**2 == c**2:
            print(a*b*c)
            flag = True
            break
    if flag:
        break
#Much better! It got the right answer in just 0.13 seconds

endTime = time.time()
totalTime = endTime - startTime
print(totalTime)