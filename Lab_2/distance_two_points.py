print ("enter the coordinates of the first point (x1, y1):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print ("enter the coordinates of the second point (x2, y2):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("the distance between the two points is:", distance)


