userList = []
userInput = None
while userInput != 0:
    userInput = int(input("Enter a integer: "))
    if userInput != 0:
        userList.append(userInput)
userList.reverse()
print(userList)
