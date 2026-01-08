#Simple types and conversions between types
i = int(input("Enter a whole number: "))
print(i)

s = input("Enter a whole Number: ")
i = int(s)
print(i)

#Converting numbers as string into integers and floats
int('10.9')

f = float('10.9')
int(f)
print(f)

int(9.6)
float(8)
print(8*1.0)

#Converting numbers into string format
print(str(8.5))
print(str(3))

s = "an int %d number" % 10
print(s)

print("a float %f number" % 3.3)

print("a float %.2f number" % 3.3)
print("a float %10.2f" % 123456789.01)
print("a float %14.2f"% 123456789.01)

a = 10
b = 3.6
print("a float %f and an int %d" % (b,a))