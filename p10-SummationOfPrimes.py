#Nathan Li - 3/11/2021 - P10: Summation of Primes

import time
startTime = time.time()

primeNums = [2, 3, 5]
index = 6
#The simplest primality test is trial division: given an input number, n, check whether
#it is evenly divisible between 2 and √n.
#We choose till √n because a larger factor of n must be a multiple of a smaller factor that has already been checked
while index < 2000000:
    for prime in primeNums:
        if prime > int(index**0.5):
            primeNums.append(index)
            index += 1
            break
        elif index % prime == 0:
            index += 1
            break
        else:
            pass
    else:
        primeNums.append(index)
        index += 1

print(sum(primeNums))
endTime = time.time()
totalTime = endTime - startTime
print(totalTime)