'''
Write  a  program  to  determine  area  and  circumference  of  circle.
Also  find  area  and  volume  of  cylinder

1) What  is  the  area  of  circle ?  --->  3.14159 * r ^ 2

2) What  is  the  circumference  of  circle ?  --->  2 * 3.14159 * r

3) What  is  the  area  of  cylinder ?  --->  2 * 3.14159  r ^ 2 + 2 * 3.14159 * r * h

4) What  is  the  volume  of  cylinder ?  --->  3.14159 * r ^ 2 *  h

5) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite
'''
import  math
class   circle:
	def   get(self):
	    self. r = float(input('Enter Radius of the circle : '))# How  to  read  radius  into  object  self
	def   area(self):
		return  math . pi * self . r ** 2 # area  of  circle
	def   cir(self):
		return  2 * math . pi * self. r # perimeter  of  circle
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		super() . get() # How  to  read  radius  into  object  self
		self. h = float(input('Enter height of the cylinder : '))# How  to  read  height  into  object  self
	def  area(self):
		return 2 * super() . area() + super() . cir() * self . h # area  of  cylinder
	def  volume(self):
		return   super() . area() * self . h # volume  of  cylinder
# End of cylinder class
def    menu():
	print('1 . Circle')
	print('2 . Cylinder')
	print('3 . Exit')
#end of menu function
menu()
ch = eval(input('Enter choice : '))
while  ch != 3 : # Repeat  until  user  input  is  3
	match  ch:
		case  1:
				c = circle()
				c . get()   # How  to  read  raidus  into  circle  object
				print('Area  :  ' ,  c . area())
				print('Circumference :  ' ,  c . cir())
		case  2:
				y = cylinder()
				y . get()  # How  to  read  raidus  and  height  into  cylinder  object
				print('Area : ' ,  y.area())
				print('Volume :  ' ,  y.volume())
	#end  of  match
	menu()
	ch = eval(input('Enter choice : '))
print('Bye')




'''
1) What  is  the  issue  with  self . area()  in  area()  method  of  cylinder  class  ? --->
																Same  class (i.e. cylinder  class) method  is  executed  and  leads  to  recursion

2) What  is  the  issue  with  self . area()  in  volume()  method  ?  --->
										Same  class(i.e. cylinder  class)  area()  method  is  executed  and  leads  to  incorrect  result

3) Can  super() . cir()  be  replaced  with  self . cir()  in  area()  method  of  cylinder  class  ?  --->
															Yes  becoz  there  is  no  cir()  method  in  cylinder  class  and
															hence  parent  class  cir()  method  executed
'''