import math
try:
    userInput = float(input("Enter a number: "))
except ValueError:
    print("Enter a number!")
    exit()
help(math.ceil)
help(math.pow)
help(math.sqrt)
help(math.log)
help(math.log10)

try:
    print(f"Absolute Value: {math.ceil(userInput)}")
except:
    print("Cannot be calculated")
try:
    print(f"Squared: {math.pow(userInput, 2)}")
except:
    print("Cannot be calculated")
try:
    print(f"Cube: {math.pow(userInput, 3)}")
except:
    print("Cannot be calculated")
try:
    print(f"Square root: {math.sqrt(userInput)}")
except:
    print("Cannot be calculated")
try:
    print(f"Natural Logarithm: {math.log(userInput)}")
except:
    print("Cannot be calculated")
try:
    print(f"Base 10 logarithm: {math.log10(userInput)}")
except:
    print("Cannot be calculated")
