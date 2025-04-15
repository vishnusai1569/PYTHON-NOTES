# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))#<class 'reversed'>
for  x  in   b:
	print(x)
	time . sleep(1)

"""
<class 'reversed'>
True
Hyd
10.8
25
"""