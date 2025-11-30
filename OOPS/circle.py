class Circle():

    # Class object attribute - shared by all Circle objects

    pi = 3.14

    def __init__(self , radius = 1):

        self.radius = radius                       # Instance attribute, unique for each object
        self.area = self.pi * radius * radius      # Instance attribute, calculated using class attribute

    def circumference(self):

        return self.radius * 2 * self.pi

mycircle = Circle(25)

print(f"Radius : {mycircle.radius}")
print(f"Area   : {mycircle.area}")
print(f"Circumference : {mycircle.circumference()}")
