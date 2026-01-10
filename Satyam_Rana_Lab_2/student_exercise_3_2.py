#3.2
import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
s = (a + b + c)/ 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"Area: {area}")