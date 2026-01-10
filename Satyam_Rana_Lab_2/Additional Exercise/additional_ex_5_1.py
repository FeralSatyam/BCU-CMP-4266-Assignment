number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))
number3 = float(input("Enter number 3: "))
if(number1 < number2 and number1 < number3):
    print(f"{number1} is the smallest number")
elif (number2 < number1 and number2 < number3):
    print(f"{number2} is the smallest number")
else:
    print(f"{number3} is the smallest number")
