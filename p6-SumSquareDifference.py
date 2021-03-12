#Nathan Li - 3/11/2021 - P6: Sum Square Difference

sumSquare = 0
squareSum = 0
numbers = range(1,101)
for x in numbers:
    sumSquare += x**2
    squareSum += x
squareSum = squareSum**2
print(squareSum - sumSquare)