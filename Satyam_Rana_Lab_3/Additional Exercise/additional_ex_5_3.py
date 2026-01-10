#5.3
sum = 0
n = int(input("Enter a number: "))
if(n<0):
    print("Enter a positive number!")
else:
    for i in range(1, n+1, 2):
        sum = sum + i

print(f"Sum is: {sum}")
