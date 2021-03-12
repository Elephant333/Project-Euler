#Nathan Li - 3/10/2021 - P4: Largest Palindrome Product

import time
startTime = time.time()

palindromes = []
for x in range(100, 1000):
    for i in range(100, 1000):
        num = str(x * i)
        if len(num) == 6:
            if num[0] == num[5] and num[1] == num[4] and num[2] == num[3]:
                palindromes.append(int(num))
        elif len(num) == 5:
            if num[0] == num[4] and num[1] == num[3]:
                palindromes.append(int(num))

endTime = time.time()
totalTime = endTime - startTime
print(totalTime)

print(max(palindromes))