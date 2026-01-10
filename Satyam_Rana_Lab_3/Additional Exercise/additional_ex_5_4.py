#5.4
run_program = True
i = 0
while run_program:
    n = input("Enter a number or stop: ")
    if n == 'stop':
        run_program = False
    else:
        n = int(n)
        if i == 0:
            i += 1
        elif i == 1:
            smallest_int = n
        else:
            if n < smallest_int:
                smallest_int = n
print(f"The smallest int is: {smallest_int}")