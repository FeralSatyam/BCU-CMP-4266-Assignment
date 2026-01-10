import math
import sys
prime_numbers = []
found_solution = False
n = int(input("Enter a number: "))
if n % 2 != 0:
     print("The number should be even!")
     sys.exit()
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
for i in prime_numbers:
     for j in prime_numbers:
          if j+1 == prime_numbers[-1]:
               break
          else:
               if(i + (j+1) == n):
                    print(f"The sum of the number is {i} and {j + 1}")
                    found_solution = True
if found_solution == False:
     print("The number can not be added by any 2 prime numbers")