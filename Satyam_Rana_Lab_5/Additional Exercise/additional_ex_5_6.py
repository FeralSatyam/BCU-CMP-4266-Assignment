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