#5.2
height = int(input("Enter height: "))
width = int(input("Enter width: "))
for i in range(1, height+1):
    for j in range(1, width+1):
        if i == 1 or i == height:
            print("*", end="")
        else:
            if j == 1 or j == width:
                print("*", end="")
            else:
                print(" ", end="")
    print("")

