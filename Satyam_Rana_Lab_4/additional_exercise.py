# #5.2
# def number(n1):
#     myAnswer = []
#     n1 = str(n1)
#     myList = list(n1)
#     for i in myList:
#         i = int(i)
#         if i% 2 == 1:
#             myAnswer.append(str(i))
#     print(myAnswer)

# user_number = int(input("Enter a number: "))
# number(user_number)


#5.3
# def check_perfect(n1):
#     sum = 0
#     i = 1
#     while i < n1:
#         if n1 % i == 0:
#             sum = sum + i
#         i += 1
#     if n1 == sum:
#         print(f"{n1} is a perfect number")
#     else:
#         print(f"{n1} is not a perfect number")

# user_number = int(input("Enter a number: "))
# check_perfect(user_number)

#5.3
# def menu():
#     print("Select and option:")
#     print("1 Add")
#     print("2 Subtract")
#     print("3 Multiply")
#     print("4 Divide")
#     print("5 Quit")
#     print(" ")
#     choice = input("Enter your choice(1/2/3/4/q): ") 

#     if (choice == 'q' or choice =='Q'):
#         calculator(choice)
#     else:
#         try:
#             choice = int(choice)
#             if(1 <= choice <= 4):
#                 calculator(choice)
#             else:
#                 print("Error: invalid choice.")
#         except:
#             print("Error: invalid choice.")
        
# def add():
#     num1 = float(input("Enter number 1: "))
#     num2 = float(input("Enter number 2: "))
#     result = num1 + num2
#     print(f"Results: adding {num1} by {num2} = {result}")
# def subtract ():
#     num1 = float(input("Enter number 1: "))
#     num2 = float(input("Enter number 2: "))
#     result = num1 - num2
#     print(f"Results: subtracting {num1} by {num2} = {result}")
# def multipy():
#     num1 = float(input("Enter number 1: "))
#     num2 = float(input("Enter number 2: "))
#     result = num1 * num2
#     print(f"Results: multiplying {num1} by {num2} = {result}")
# def divide ():
#     num1 = float(input("Enter number 1: "))
#     num2 = float(input("Enter number 2: "))
#     if num2 == 0:
#         print("Error: cannot divide by 0")
#     result = num1 / num2
#     print(f"Results: dividing {num1} by {num2} = {result}")
# def calculator(choice):
#     match (choice):
#         case 1:
#             print("You selected 1.")
#             add()
#         case 2:
#             print("You selected 2.")
#             subtract()
#         case 3:
#             print("You selected 3.")
#             multipy()
#         case 4:
#             print("You selected 4.")
#             divide()
#         case 'q':
#             print("You selected q.\nBye!")
#         case 'Q':
#             print("You selected Q.\nBye!")

# menu()

