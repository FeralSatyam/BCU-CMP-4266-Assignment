import math

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        """Return Euclidean distance between two points."""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

    def __repr__(self):
        return f"Coordinate({self.x}, {self.y})"


class Rectangle:
    def __init__(self, top_left, bottom_right):
        """top_left and bottom_right are Coordinate objects."""
        self.top_left = top_left
        self.bottom_right = bottom_right

        self.width = abs(self.bottom_right.x - self.top_left.x)
        self.height = abs(self.top_left.y - self.bottom_right.y)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def contains_point(self, point):
        """Check if a Coordinate lies inside or on the border."""
        return (self.top_left.x <= point.x <= self.bottom_right.x and
                self.bottom_right.y <= point.y <= self.top_left.y)

    def __repr__(self):
        return f"Rectangle({self.top_left}, {self.bottom_right})"
def test_geometry():
    print("Testing Coordinate and Rectangle classes")

    tl = Coordinate(2, 8)  
    br = Coordinate(10, 2)     

    print("Top-left point:", tl)
    print("Bottom-right point:", br)
    print("Distance between tl and br:", tl.distance(br))

    rect = Rectangle(tl, br)
    print("Rectangle:", rect)

    print("Width:", rect.width)
    print("Height:", rect.height)
    print("Area:", rect.area())
    print("Perimeter:", rect.perimeter())

    inside = Coordinate(5, 5)
    outside = Coordinate(20, 20)
    print("Point", inside, "inside?", rect.contains_point(inside))
    print("Point", outside, "inside?", rect.contains_point(outside))


if __name__ == "__main__":
    test_geometry()
