#5.3
def check_perfect(n1):
    sum = 0
    i = 1
    while i < n1:
        if n1 % i == 0:
            sum = sum + i
        i += 1
    if n1 == sum:
        print(f"{n1} is a perfect number")
    else:
        print(f"{n1} is not a perfect number")

user_number = int(input("Enter a number: "))
check_perfect(user_number)
