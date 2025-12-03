class Cylinder:

    def __init__(self , height = 1 , radius = 1):

        self.height = height
        self.radius = radius

    def volume(self):
        
        return 3.14 * self.radius * self.radius * self.height

    def surface_area(self):

        return 2 * 3.14 * self.radius*(self.height + self.radius)


c = Cylinder(2,3)

v = c.volume()
s = c.surface_area()

print("Volume : ",v)
print("Surface area : ",s)
