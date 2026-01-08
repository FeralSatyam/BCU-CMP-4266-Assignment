# #2.1.1
amount1 = float(input("Enter Amount 1: "))
amount2 = float(input("Enter Amount 2: "))
amount1 *= 0.8
amount2 *= 0.9
tax = amount1 *0.3 + amount2 *0.2
total = amount1 + amount2 + tax
print(tax)
print(f"Total Cost: ${total}")

#Table
#amount1     amount2    tax  total
#10          40          9.6   53.6
#20          30         10.2    53.2
#60          70         27.0    138.0
#50         50          21.0    106.0



#2.1.2
print(3*'Yes',2*'!') # YesYesYes !!
print(3*'Yes'+2*'!') # YesYesYes!!
print(2**2**3) # 256
print(2**(2**3)) # 256
print(10//3**2+(2%3)) # 3

#2.1.3
print(3*2) # 6
print(type(3*2)) #type - int
print('3' + '2') # 32
print(type('3' + '2')) # type - str
print('3' * 2) # 33
print(type('3' * 2)) # type - str
print(3/2) # 1.5
print(type(3/2)) # float
print(3//2) # 1
print(type(3//2)) # int
print(3 + 2.0) # 5.0
print(type(3 + 2.0)) # float
print(3 > 2) # True
print(type(3 > 2)) # bool
print(3 != 2) # True
print(type(3 != 2)) # bool
print(4 == 2**2) # True
print(type(4 == 2**2)) # bool
print(3>2 and 10 > 11) # False
print(type(3>2 and 10 > 11)) # bool
print(3>2 and not(10>11)) # True
print(type(3>2 and not(10>11))) # bool
print(format(5.1,'.2f')) #5.10
print(type(format(5.1,'.2f'))) # string
print(not(3>2 and 5<4)) # True
print(type(not(3>2 and 5<4))) # Bool


