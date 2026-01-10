n = int(input("Enter 5 digit number: "))
n = str(n)
rev_n = int(n[::-1])
n = int(n)
if n == rev_n:
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")