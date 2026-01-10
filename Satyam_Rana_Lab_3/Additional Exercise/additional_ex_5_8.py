#5.8
import math
prime_numbers = []
n = int(input("Enter a number: "))
for i in range (2, n+1):
    isPrime = True
    sqrt_of_i = int(math.sqrt(i))
    for x in range(2, sqrt_of_i+1):
        if i % x == 0:
            isPrime = False
            break
    if isPrime: 
        if i in prime_numbers:
                pass
        else:
            prime_numbers.append(i)
print(prime_numbers)