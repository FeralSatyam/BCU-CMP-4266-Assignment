base_working_hour = 40.0
working_hour = float(input("Enter your working hour: "))
wage = float(input("Enter your hourly wage: "))
if(working_hour > base_working_hour):
    ot_working_hour = working_hour - base_working_hour
    ot_wage = (wage * 20/100) * ot_working_hour 
    print(f"The employee is due additional pay: {ot_wage}")
else:
    print(f"Your total wage is: {working_hour*wage}")