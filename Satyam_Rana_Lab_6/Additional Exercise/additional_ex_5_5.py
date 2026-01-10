while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Enter a positive integer.")

primes = []

if n > 1:
    primes.append(1)
if n > 2:
    primes.append(2)

for num in range(3, n, 2):
    is_prime = True
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print("Prime list:", ", ".join(map(str, primes)))
