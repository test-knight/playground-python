class Point:
    def draw(self):
        print("draw")

    def move(self):
        print("Move")


point1 = Point()
# attributes/properties can be defined outside the class
point1.a = 10
point1.draw()
point1.move()
print(point1.a)
point1.b = 100
print(point1.b)

point2 = Point()
point2.a = "Test"
print(point2.a)


class PointInit:

    # class constructor/initializer with properties defined in them
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("draw")

    def move(self):
        print("Move")


point = PointInit(10, 20)
print(point.x, point.y)

#class with pre-formatted string input
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, this is {self.name}")


Person("Riaz").talk()
Person("Bob").talk()

