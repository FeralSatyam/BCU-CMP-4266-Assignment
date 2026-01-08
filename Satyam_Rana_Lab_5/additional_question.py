#5.1
# def print_full_pyramid(level, symbol):
#     if level <= 0:
#         print("Level must be greater than 0.")
#         return

#     for i in range(1, level + 1):
#         spaces = ' ' * (level - i)
#         symbols = symbol * (2 * i - 1)
#         print(spaces + symbols)
# print_full_pyramid(5, "*")

#5.2
# def have_common_member(list1, list2):
#     for item in list1:
#         if item in list2:  
#             return True
#     return False
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]

# if have_common_member(list1, list2):
#     print("The lists have at least one common member.")
# else:
#     print("The lists do not have any common members.")

#5.3
def find_greater(x_list, x_num):
    result = []
    for item in x_list:
        if item > x_num:
            result.append(item)
    return result

print(find_greater([11, 35, 4, 67, 23], 20))

#5.4
def sum(list_x, list_y):
    result = []
    for i in range(len(list_x)):
        result.append(list_x[i] + list_y[i])
    return result

print(sum([2, 4, 7], [1, 2, 3]))

#5.5
def word_frequencies(list_a):
    freq = {}
    for word in list_a:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

print(word_frequencies(["apple", "banana", "apple", "orange", "banana", "apple"]))

#5.6
import math

def get_next_point(step):
    x = input(f"Enter x{step}: ")
    y = input(f"Enter y{step}: ")
    if x.lower() == "trace" or y.lower() == "trace":
        return "trace"
    return (int(x), int(y))

def cal_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def get_direction(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    direction = ""

    if dy > 0:
        direction += "Top "
    elif dy < 0:
        direction += "Bottom "

    if dx > 0:
        direction += "Right"
    elif dx < 0:
        direction += "Left"

    return direction.strip()

def trace(distances, directions):
    print("------ Trace of Robot Movement ------")
    total = 0
    for i, (d, dirc) in enumerate(zip(distances, directions), start=1):
        print(f"Step {i}: {d:.2f} units, Direction: {dirc}")
        total += d
    print(f"Total distance travelled: {total:.2f} units")

def main():
    print("------ Robot Program ------")
    current_point = (0, 0)
    step = 1
    distances = []
    directions = []

    while True:
        print("----------")
        next_point = get_next_point(step)

        if next_point == "trace":
            trace(distances, directions)
            continue

        if next_point == (999, 999):
            break

        distance = cal_distance(current_point, next_point)
        direction = get_direction(current_point, next_point)

        distances.append(distance)
        directions.append(direction)

        current_point = next_point
        step += 1
        print("----------")

    print("------ Distances ------")
    for i, (d, dirc) in enumerate(zip(distances, directions), start=1):
        print(f"Step {i}: {d:.2f} units, Direction: {dirc}")
    print(f"Total distance travelled: {sum(distances):.2f} units")

if __name__ == "__main__":
    main()