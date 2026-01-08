import math
#1 Roots of a Quadratic Equation
A = float(input("Enter the value of A: "))
B = float(input("Enter the value of B: "))
C = float(input("Enter the value of C: "))
print(f"The value of A is {A}, B is {B} and C is {C}")
d = math.sqrt(B*B-4*A*C)
root1 = (-B+d)/(2*A)
root2 = (-B-d)/(2*A)
print(f"The value of root 1 is {root1} and root 2 is {root2}")
quit()


#Test your completed program
# A = 1, B = 0, C = -2
# root1 = 2.0, root2 = -2.0

#A = 1, B = 5, C = -36
#root1 = 4.0, root2 = -9.0

#A = 2, B = 7.5, C = 6
#root1 = -1.1569296691827464, root2 = -2.5930703308172536

#A = 0, B = 3.5, C = 8
#results error since A can not be zero