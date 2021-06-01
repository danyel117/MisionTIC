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
numberToEvaluate = 1
while contPrimeNumbers < 10:
    if isPrimeNumber(numberToEvaluate):
        contPrimeNumbers = contPrimeNumbers + 1
        print(numberToEvaluate)
    
    numberToEvaluate = numberToEvaluate + 1


#identificar la primera secuencia de números primos cuya suma
#también es prima