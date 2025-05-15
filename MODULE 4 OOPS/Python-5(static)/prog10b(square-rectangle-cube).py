'''
Write  a  program  to  determine  area  and  perimeter  of  rectangle  and  square.
Also  find  surface  area  and  volume  of  cube

1) What  is  the  area  of  square ?  --->  a ^ 2

2) What  is  the  perimeter  of  square ?  --->  4 *  a

3) What  is  the  area  of  rectangle ?  --->  a * b

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (a + b)

5) What  is  the  surface  area  of  cube ? --->  6 * a ^ 2

6) What  is  the  volume  of  cube  ?  --->  a ^ 3

7) Reuse  parent  class  methods  in  child   classes  but  do  not  rewrite
'''
class   Square:
	def   get(self):
		self . a = float(input('Enter a Side : '))# How  to  read  side  of  square
	def   area(self):
		return  self. a ** 2 # area  of  square
	def   peri(self):
		return  4 * self . a # perimeter  of  square
class   Rectangle(Square):
	def   get(self):
		super() . get() # How  to  read  length  of  rectangle
		self . b = float(input('Enter Breadth : ')) # How  to  read  breadth  of  rectangle
	def   area(self):
		 return  self . a * self . b # area  of  rectangle
	def   peri(self):
		return   2 * (self . a + self . b) # perimeter  of   rectangle
class   Cube(Square):
	def   get(self):
		 super() . get() # How  to  read  side  of  cube
	def   area(self):
		return   6 * super() . area() # area  of  cube
	def   volume(self):
		return   super() . area() * self . a # volume  of  cube
def  menu():
	print('1 . Square')
	print('2 . Rectangle')
	print('3 . Cube')
	print('4 . Exit')
# End  of  the  function
menu()
ch = int(input('Enter  choice : '))
while  ch != 4 : # repeat  until  user  input  is  4
	match   ch:
		case   1:
			s = Square()
			s . get()  # How  to  read  side  into   square  object  's'
			print('Area   :  ' ,  s.area())
			print('Perimeter  :  ' ,  s.peri())
		case   2:
			r = Rectangle()
			r . get()  # How  to  read  length  and  breadth  into   rectangle  object  'r'
			print('Area  :  ' ,  r.area())
			print('Perimeter  :  ' ,  r.peri())
		case   3:
			c = Cube() # How  to  read  side  into  cube  object  'c'
			c . get()  # How  to  read  side  into  cube  object  'c'
			print('Area  :   ' ,  c . area())
			print('Volume  :  ' ,  c . volume())
	menu()
	ch = int(input('Enter  choice : '))