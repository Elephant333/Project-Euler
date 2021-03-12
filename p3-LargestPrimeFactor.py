#Nathan Li - 3/10/2021 - P3: Largest Prime Factor

import time
startTime = time.time()

num = 600851475143

for x in range(2, num//2 + 1): #dividing by two to reduce test size, can do this because only evenly divisible if less than half
    while num % x == 0:
        num = num / x
        if num == 1 or num == x:
            print(x)
            endTime = time.time()
            totalTime = endTime - startTime
            print(totalTime)
            break

#takeaway: this is essentially doing a number tree, and I didn't realize that cause I haven't done one in so long