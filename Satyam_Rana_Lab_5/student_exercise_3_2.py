#3.2
import math

def get_next_point(step):
    x = int(input(f"Enter x{step}: "))
    y = int(input(f"Enter y{step}: "))
    return (x, y)

def cal_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def main():
    print("------ Robot Program ------")
    current_point = (0, 0)
    step = 1
    distances = []

    while True:
        print("----------")
        next_point = get_next_point(step)
        if next_point == (999, 999):
            break
        distance = cal_distance(current_point, next_point)
        distances.append(distance)
        current_point = next_point
        step += 1
        print("----------")

    print("------ Distances ------")
    for i, d in enumerate(distances, start=1):
        print(f"Step {i}: {d:.2f} units")

if __name__ == "__main__":
    main()