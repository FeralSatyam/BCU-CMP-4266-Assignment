#5.1
def print_full_pyramid(level, symbol):
    if level <= 0:
        print("Level must be greater than 0.")
        return

    for i in range(1, level + 1):
        spaces = ' ' * (level - i)
        symbols = symbol * (2 * i - 1)
        print(spaces + symbols)
print_full_pyramid(5, "*")