
#3.1
# import math
# n = int(input("Enter a number: "))
# isPrime = True
# sqrt_of_n = int(math.sqrt(n))

# if n > 1:
#     for i in range(2, sqrt_of_n+1):
#         if n % i == 0:
#             isPrime = False
#             break
# else:
#     print("Enter a number greater than 2")

# if isPrime:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")
#     for i in range(2, n):
#         if n % i == 0:
#             print(f"Divisible by: {i}")
    


#3.2
print("*******WELCOME TO OUR BANK*******")

user_name=input(("Please enter your name: "))

balance = 1000.0
op=True

while op: #student completes while loop
    print("\n\n Choose 1 for Deposit \n Choose 2 for Withdraw \n Choose 3 for Check Balance \n Choose Q or q to Exit:")
    choice = input("Please choose transactions:")
    if choice == "1": #user chooses 'deposit'
         amount = float(input("Enter the amount you want to deposit: "))
         balance = balance + amount
         print("Deposit Sucessful!")
    elif choice == "2":
       amount = float(input("Enter the amount you want to withdraw: "))
       if(balance - amount < 0):
           print("It is not possible to withdraw beyond the account balance")
       else:
           balance = balance - amount
           print("Withdrawl Sucessful!")
           
        
    elif choice=="3":
        print(f"Your balance is: {balance}")
      
    elif choice == 'q' or choice == 'Q':
        
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        op= False
    else:
        print("Wrong transaction! Try again.")


