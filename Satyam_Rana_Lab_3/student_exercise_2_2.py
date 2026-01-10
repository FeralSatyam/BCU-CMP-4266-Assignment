#2.2
total = 0
for number in range(9, 20):
    if number % 2 == 0 or number % 3 == 0:
        total = total + 1
print(total)
