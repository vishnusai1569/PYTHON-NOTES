x=int(input("Enter  value  of  x  co-ordinate : "))
y=int(input("Enter  value  of  y  co-ordinate : "))
if x>0 and y>0:
	print("1st  quadrant ")
elif x<0 and y>0:
    print("2dn  quadrant ")
elif x<0 and y<0:
    print("3rd  quadrant ")
elif x>0 and y<0:
    print("4th  quadrant ")
elif (x<0 or x>0) and y==0:
    print("x - axis ")
elif x==0 and (y<0 or y>0):
    print("y - axis ")
else :
    print("origin")