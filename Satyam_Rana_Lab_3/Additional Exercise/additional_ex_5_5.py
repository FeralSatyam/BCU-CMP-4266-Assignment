#5.5
n = int(input("Enter a 3 digit int: "))
if len(str(n)) == 3:
    print(f"Second digit from left: {str(n)[1:2]}")
    print(f"Third digit from right: {str(n)[-4:-2]}")
else:
    print("Enter a 3 digit number!")