tuplex = (4, 9, ['a', 'b'], 123.45, 0)
print("Initial:", tuplex)

lst = list(tuplex)
lst.append(7)
tuplex = tuple(lst)
print("Step 1:", tuplex)

lst = list(tuplex)
lst.insert(3, (10, 100, 1000))
tuplex = tuple(lst)
print("Step 2:", tuplex)

lst = list(tuplex)
lst.insert(2, "bob")
tuplex = tuple(lst)
print("Step 3:", tuplex)

lst = list(tuplex)
lst.insert(0, 3.5)
tuplex = tuple(lst)
print("Step 4:", tuplex)

lst = list(tuplex)
lst.insert(-1, False)
tuplex = tuple(lst)
print("Step 5:", tuplex)

lst = list(tuplex)
lst.remove(9)
tuplex = tuple(lst)
print("Step 6:", tuplex)

lst = list(tuplex)
del lst[-4]
tuplex = tuple(lst)
print("Step 7:", tuplex)
