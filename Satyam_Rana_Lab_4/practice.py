import math
# def print_name(first, last):
#     print("First name %s" %first)
#     print("Last name %s" %last)

# fn = "Albert"
# ln = "Einstein"
# print_name(fn, ln)

# def change_val(num):
#     num += 100
#     print("Inside parameter value %d" %num)

# val = 100
# print("Argument value %d" %val)
# change_val(val)
# print("Argument value after function call %d" %val)

# def get_name():
#     first = input("Enter first name: ")
#     last = input("Enter last name: ")
#     return first, last

# f_name, l_name = get_name()
# print(f_name)
# print(l_name)

# def add_number(n1, n2):
#     summation = n1 + n2
#     print("Here is sum %d" %summation)

# add_number(10, 5)

# print(abs(-12))
# print(abs(min(max(-12, 5), -15)))
#print(min(sum(range(1, 10, 2)),sum(range(2, 10, 2))))
# print(len("This is a test"))

# print(max(math.trunc(-6.6), math.floor(-6.6)))

def mystery1(a, b):
    return a+b
def mystery2(a, b):
    if a > b:
        return a
    else:
        return b
def mystery3(a, b):
    if a < b:
        print(a)
        a = a + 2
        mystery3(a, b)
    
y = mystery1(10, 8)
print(y)
y = mystery2(10, 8)
print(y)
mystery3(10, 22)
