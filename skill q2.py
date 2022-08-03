import math
def Circle(r):
    area=math.pi*r*r
    perimeter=math.pi*2*r
    s="area = ",area,"perimeter = ",perimeter
    return s
def Rectangle(a,b):
    area =a*b
    perimeter=2*(a+b)
    s=("area = ", area,"perimeter = ", perimeter)
    return s
def Triangle(x,y,z):
    s= (x+y+z) / 2
    area = (s * (s - x) * (s - y) * (s - z)) ** 0.5
    perimeter =x+y+z
    d=("area = ", area,"perimeter = ", perimeter)
    return d
print("1.Circle/n2.Rectangle/n3.Triangle/n")
n=int(input("enter number of terms :"))
if n==1:
    r=int(input("enter the radius :"))
    p = Circle(r)
elif n==2:
    a = int(input("enter the lenght :"))
    b = int(input("enter the breath :"))
    p = Rectangle(a,b)
elif n==3:
    x = int(input("enter the value :"))
    y = int(input("enter the value :"))
    z = int(input("enter the value :"))
    p = Triangle(x,y,z)
else:
    print("enter valid inputs")
print(p)



