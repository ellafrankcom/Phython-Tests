#Practice 2, Q1
import math
class circle_at:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_r(self, r):
        self.r = r

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_r(self):
        return self.r

    def display(self):
        print("Your circle attributes are {:0.3f} {:0.3f} and {:0.3f}".format(self.x, self.y, self.r))

class circle(circle_at):
    def __init__(self, x = 0.0, y = 0.0, r = 0.0):
        super().__init__(x, y, r)
        self.area = 0.0

    def distance(self, obj1):
        dist = math.sqrt(((self.get_x() - obj1.get_x())**2) + (self.get_y() - obj1.get_y())**2)
        if (dist > self.get_r() + obj1.get_r()):
            return 0, dist
        elif (dist == self.get_r() + obj1.get_r()):
            return 1, dist
        else:
            return -1, dist

    def areac(self, obj1 = None):
        if obj1 == None:
            return math.pi * self.get_r()**2
        else:
            return math.pi * obj1.get_r()**2

x1 = circle_at(3,4,9)
x1.display()
x2 = circle(2,4,7)
x2.display()
print(x2.distance(x1))
print(x2.areac())
print(x2.areac(x1))
        
