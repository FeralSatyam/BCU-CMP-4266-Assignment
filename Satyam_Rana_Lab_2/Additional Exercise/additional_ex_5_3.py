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