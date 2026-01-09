# #3.1
# year = int(input("Enter a year to check if it is a leap year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year, {year} is divisble by 4 and 100 but not divisible by 400")
#     else:
#         print(f"{year} is not a leap year, {year} is divisble by 4 but not by 100")
# else:
#     print(f"{year} is not a leap year, {year} is not divisible by 4")


#3.2
import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
s = (a + b + c)/ 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"Area: {area}")