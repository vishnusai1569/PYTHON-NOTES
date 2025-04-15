import math
x=int(input("Enter  value  of  x :"))
y=int(input("Enter  value  of  y :"))
r=int(input("Enter  value  of  r :"))
d=math.sqrt(x**2+y**2)
print(d)
if d>r:
    print("Outside  the  circle")
elif d<r:
    print("Inside the circle")
else:
    print("On the circle")