class Point:
    def __init__(self, x, y):
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)

point2 = Point()
point2.x = 1
print(point2.x)