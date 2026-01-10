
# # 3.1
import math
n = int(input("Enter a number: "))
isPrime = True
sqrt_of_n = int(math.sqrt(n))

if n > 1:
    for i in range(2, sqrt_of_n+1):
        if n % i == 0:
            isPrime = False
            break
else:
    print("Enter a number greater than 2")

if isPrime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
    for i in range(2, n):
        if n % i == 0:
            print(f"Divisible by: {i}")
    


