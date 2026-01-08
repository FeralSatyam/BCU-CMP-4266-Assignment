#5.1
# for i in range (1, 101):
#     print(f"Square of {i} is: {i*i}")

#5.2
# height = int(input("Enter height: "))
# width = int(input("Enter width: "))
# for i in range(1, height+1):
#     for j in range(1, width+1):
#         if i == 1 or i == height:
#             print("*", end="")
#         else:
#             if j == 1 or j == width:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#     print("")


#5.3
# sum = 0
# n = int(input("Enter a number: "))
# if(n<0):
#     print("Enter a positive number!")
# else:
#     for i in range(1, n+1, 2):
#         sum = sum + i

# print(f"Sum is: {sum}")

#5.4
# run_program = True
# i = 0
# while run_program:
#     n = input("Enter a number or stop: ")
#     if n == 'stop':
#         run_program = False
#     else:
#         n = int(n)
#         if i == 0:
#             i += 1
#         elif i == 1:
#             smallest_int = n
#         else:
#             if n < smallest_int:
#                 smallest_int = n
# print(f"The smallest int is: {smallest_int}")

#5.5
# n = int(input("Enter a 3 digit int: "))
# if len(str(n)) == 3:
#     print(f"Second digit from left: {str(n)[1:2]}")
#     print(f"Third digit from right: {str(n)[-4:-2]}")
# else:
#     print("Enter a 3 digit number!")

#5.7
# n = int(input("Enter the no till where the fibbo sequence will work: "))
# num1 = 0
# num2 = 1
# print(num1)
# print(num2)
# for i in range(n):
#     sum = num1 + num2
#     print(sum)
#     num1 = num2
#     num2 = sum


#5.8
# import math
# prime_numbers = []
# n = int(input("Enter a number: "))
# for i in range (2, n+1):
#     isPrime = True
#     sqrt_of_i = int(math.sqrt(i))
#     for x in range(2, sqrt_of_i+1):
#         if i % x == 0:
#             isPrime = False
#             break
#     if isPrime: 
#         if i in prime_numbers:
#                 pass
#         else:
#             prime_numbers.append(i)
# print(prime_numbers)

#5.9
#5.9 Extend Exercise 3.2. The Goldbach conjecture asserts that every even number is the sum of two
# prime numbers. Modify the program written in 3.2 that gets a number from the user, checks to
# make sure that it is even, and then finds two prime numbers that add up to it.

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