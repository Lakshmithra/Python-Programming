# Program to calculate the area of the circle 

def calculatearea(r):
    pi = 3.14
    area = pi * r * r
    return area
  
radius = float(input("Enter the radius of the circle : "))
a = calculatearea(radius)
print(f"Area of the circle : {a}")
