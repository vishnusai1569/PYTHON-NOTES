# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1() #  Object  is  initialized  with  x = 10 , y = 20 , z = 30  by  constructor
b = c1()   #  Object  is  initialized  with  x = 10 , y = 20 , z = 30  by  constructor
print(a . __dict__)  #  {'x' : 10 , 'y' : 20 , 'z' : 30}
print(b . __dict__) #  {'x' : 10 , 'y' : 20 , 'z' : 30}
del  a . x  #  Removes  variable  'x' from  object  'a'
del  b . y  #  Removes  variable  'y' from  object  'b'
print(a . __dict__)   #  {'y' : 20 , 'z' : 30}
print(b . __dict__)   #  {'x' : 10 , 'z' : 30}
print(a . x)  #  Error :  No  variable   'x'  in  object  'a'
print(b . y)   #  Error :  No  variable   'y'  in  object  'b'



'''
1) What  does  del  a . x  do ?  --->  Removes  variable  'x'  of  object   'a'

2) What  does  del   a   do ?   --->  Deletes  object  'a'

3) The  above  program  demonstrates  that  python  object  is  shrinkable
'''