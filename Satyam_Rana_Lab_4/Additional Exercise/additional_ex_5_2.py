#5.2
def number(n1):
    myAnswer = []
    n1 = str(n1)
    myList = list(n1)
    for i in myList:
        i = int(i)
        if i% 2 == 1:
            myAnswer.append(str(i))
    print(myAnswer)

user_number = int(input("Enter a number: "))
number(user_number)