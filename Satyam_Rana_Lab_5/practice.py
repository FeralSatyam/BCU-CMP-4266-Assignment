import math
print(type(("a",10.5)))
print(type((0)))
print(type(()))
print(type("Hello"))
print(type(10.5))
print(type(math.pi) == type(10.5))
print(type(10.5) == type("hello"))
print(type([]))
print(type([2,4]))
print(type(['hello', 10.5]))

l = [2, 3]
l.append(5)
print(l)

l.insert(2, 4)
print(l)

print(l[1])
# print(l[4])

print(len(l))
print(len("this"))
print(len((0,)))
l.reverse()
print(l)

l.sort()
print(l)

# del l[1]
# print(l)
del l[3]
print(l)

print(list(range(1,10)))

print(list(range(1,20,2)))

print(list(range(3, 20, 3)))
print(list(range(20, 0, -1)))
a = list(range(1,11))
print(a)
print(a[3:5])
print(a[:])
print(a[:6])
print(a[6:])

b=a
c=a[:]
a.remove(3)
print(a)
print(b)
print(c)

a = [5, 10, 15, 20, 25]
def first_last(input_list):
    return [input_list[0], input_list[-1]]
print(first_last(a))