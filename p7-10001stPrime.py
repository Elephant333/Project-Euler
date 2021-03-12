#Nathan Li - 3/11/2021 - P7: 10,001st Prime

primeNums = [2, 3, 5]
index = 6
#The simplest primality test is trial division: given an input number, n, check whether
#it is evenly divisible between 2 and √n
while len(primeNums) < 10001:
    for prime in primeNums:
        if index % prime == 0:
            index += 1
            break
        else:
            pass
    else:
        primeNums.append(index)
        index += 1

print(primeNums[-1])