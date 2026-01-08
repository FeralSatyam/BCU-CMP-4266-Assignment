# #2 Population standard deviation
import math
temp = 0
myList = []
for i in range(5):
    n = int(input(f"Enter {i+1} number: "))
    myList.append(n)
mean = sum(myList)/len(myList)
N = len(myList)
for x in myList:
    temp += (x-mean)**2
sd = math.sqrt(temp/N)
print(sd)