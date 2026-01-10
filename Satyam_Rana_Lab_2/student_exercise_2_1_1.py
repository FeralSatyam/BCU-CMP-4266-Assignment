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
