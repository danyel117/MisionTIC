def isPrimeNumber(number):
    #retornar True si el numero es primo. False si no es primo.
    if number == 1 or number==0:
        return False
    isPrime = True
    for divisor in range(2,number):
        if number % divisor == 0:
            isPrime = False
            return isPrime
    return isPrime


contPrimeNumbers = 0
sumPrimeNumbers = 0
numberToEvaluate = 1
sumPrimeFound = False
while not sumPrimeFound:
    if isPrimeNumber(numberToEvaluate) == True:
        contPrimeNumbers = contPrimeNumbers + 1
        sumPrimeNumbers  = sumPrimeNumbers + numberToEvaluate
        print(numberToEvaluate, sumPrimeNumbers, isPrimeNumber(sumPrimeNumbers))
        if isPrimeNumber(sumPrimeNumbers) and contPrimeNumbers>=2:
            sumPrimeFound = True
    
    numberToEvaluate = numberToEvaluate + 1
