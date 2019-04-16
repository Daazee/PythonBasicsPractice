def isPrimeNumber(numToCheck):
    result = False
    res = []
    remainders = []
    if(numToCheck == 1):
        numToCheck = numToCheck + 1
        result = True
        res.append(result)
        res.append(numToCheck)
        return res

    initialDisvisor =2
    for j in range(initialDisvisor,numToCheck):
        remainder = numToCheck % j
        remainders.append(remainder)
    if 0 not in remainders:
        numToCheck = numToCheck + 1
        result = True
        res.append(result)
        res.append(numToCheck)
        return res
    else:
        numToCheck = numToCheck + 1
        isPrimeNumber(numToCheck)

k = int(input("Enter number of prime numbers to be printed: "))
numToCheck = 1
for _ in range(k):
    result = isPrimeNumber(numToCheck)
    if(result[0] == True):
        print(result[1] - 1)
    numToCheck = result[1]
