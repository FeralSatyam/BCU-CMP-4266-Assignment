number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))
myList = [number1, number2, number3]
sorted_list = sorted(myList)
n1, n2, n3 = sorted_list
print(f"{n1}, {n2}, {n3} is the sorted number")