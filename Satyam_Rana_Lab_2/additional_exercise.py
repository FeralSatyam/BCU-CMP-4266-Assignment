#5.1
number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))
number3 = float(input("Enter number 3: "))
if(number1 < number2 and number1 < number3):
    print(f"{number1} is the smallest number")
elif (number2 < number1 and number2 < number3):
    print(f"{number2} is the smallest number")
else:
    print(f"{number3} is the smallest number")



#5.2
n = int(input("Enter 5 digit number: "))
n = str(n)
rev_n = int(n[::-1])
n = int(n)
if n == rev_n:
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")

#5.3
n = int(input("Enter a number: "))
sum = 0
n = str(n)
for i in n:
    sum = sum + 1
if sum == 1:
    print(f"{n} is 1 digit number")
elif sum == 2:
    print(f"{n} is a 2 digit number")
elif sum == 3:
    print(f"{n} is a 3 digit number")
elif sum > 3:
    print(f"{n} is more than 3 digit number")
else:
    print("Enter a positive number")


#5.4
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))
myList = [number1, number2, number3]
sorted_list = sorted(myList)
n1, n2, n3 = sorted_list
print(f"{n1}, {n2}, {n3} is the sorted number")


#5.5
base_working_hour = 40.0
working_hour = float(input("Enter your working hour: "))
wage = float(input("Enter your hourly wage: "))
if(working_hour > base_working_hour):
    ot_working_hour = working_hour - base_working_hour
    ot_wage = (wage * 20/100) * ot_working_hour 
    print(f"The employee is due additional pay: {ot_wage}")
else:
    print(f"Your total wage is: {working_hour*wage}")