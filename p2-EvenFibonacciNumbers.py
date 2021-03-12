#Nathan Li - 3/10/2021 - P2: Even Fibonacci Numbers

fibUnder4Mil = [1,2]
index = 1
nextNum = 0
while nextNum < 4000000:
    fibUnder4Mil.append(fibUnder4Mil[index] + fibUnder4Mil[index - 1])
    index = index + 1
    nextNum = fibUnder4Mil[index] + fibUnder4Mil[index - 1]

evenFibUnder4Mil = []
for i in fibUnder4Mil:
    if i % 2 == 0:
        evenFibUnder4Mil.append(i)

finalSum = sum(evenFibUnder4Mil)

print(finalSum)