class Line:

    def __init__(self , coor1 , coor2):

        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]

    def distance(self):

        x = pow(self.x2 - self.x1,2)
        y = pow(self.y2 - self.y1,2)
        d = pow(x+y , 1/2)
        return d

    def slope(self):

        x = self.x2 - self.x1
        y = self.y2 - self.y1
        s = y / x
        return s

c1 = (3 , 2)
c2 = (8 , 10)
l = Line(c1 , c2)
dc = l.distance()
s = l.slope()
print("Distance : ",dc)
print("Slope : ",s)
        
