'''
Write  a  program  to  determine  area  and  perimeter  of  triangle , circle , rectangle  and  square

1) What  is  the  parent  class ?  ---> shape
    What  are  child  classes ?  ---> triangle , circle , rectangle , square

2) What  is  the  area  of  triangle  ?  --->  sqrt(s * (s - a) *  (s - b) * (s - c))
    What  is  the  value  of  's' ?  ---> (a + b + c) / 2
    What  is  the  perimeter  of  triangle ?  ---> a + b + c

3) What  is  the  area  of  circle ?  --->  3.14159 * a ^ 2  where  'a'  is  radius  of  circle
    What  is  the  circumference  of  circle ?  --->  2 * 3.14159 * a

4) What  is  the  area  of  rectangle  ?  --->  a * b  where  'a'  is  length and  'b'  is  breadth
    What  is  the  perimter  of  rectangle ?  ---> 2 * (a + b)

5) What  is  the  area  of  square ?  ---> a ^ 2
    What  is  the  perimeter  of  square  ?  ---> 4 * a
'''
import   math
from  abc  import  *
class  shape(ABC):
	def   get(self):
		self . a = float(input()) #   How  to  read  input  to  variable  'a'  of  object  self
	@abstractmethod
	def   area(self):
		pass
	@abstractmethod
	def  peri(self):
		pass
	@abstractmethod
	def  test(self):
		pass
'''
1) Is   shape()  valid ? --->
					No  becoz  shape  is  an  abstract  class  with   three  abstract  methods  area() , peri()  and  test()

2) Why  are  area() , peri()  and  test()  abstract  methods ? --->  Since  there  is  no  idea  about  the  shape

3) Who  should   implement  area(),  peri()  and  test()  methods ?  --->  Every  child  class  of  shape

4) What  is  the  advantage  of  writing  ABC  ?  --->
												Every  child  class  should  implement  all  the  abstract  methods  of  shape  class

5) What  happens  if  at  least  one  child  class  does  not  implement  abstract  methods  of  shape  class ?  --->
																									That  child  class  object  can  not  be  created
'''
class  triangle(shape):
	def   get(self):
		print('Enter  3  sides  of  triangle')
		#  How  to  read  the  3  sides  of  triangle
		super() . get()
		self . b  =  float(input())
		self . c  =  float(input())
	def   area(self):
		s = (self . a  +  self . b + self . c) / 2
		return  math . sqrt(s * (s - self . a) * (s - self . b) * (s - self . c)) #  area  of  triangle
	def   peri(self):
		return  self . a + self . b + self . c  #   perimeter  of  triangle
	def   test(self):
		if  self . a + self . b > self . c  and  self . b + self . c >  self .  a   and   self . c + self .  a > self . b:  #  sum  of  every  2  sides  should  be  >   3rd   side
				pass  #  do  nothing
		else:
			print('Not    a  triangle')
			exit() #  How  to  stop  execution
class   circle(shape):
	def   get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		super() . get()  #  How  to  read  radius
	def   area(self):
		return  math . pi * self . a  **  2   #  area  of  circle
	def   peri(self):
		return  2 * math . pi * self . a  #   circumference  of circle
	def  test(self):
		if  self . a  < 0:  #   side  is  -ve
		    print('Radius  can  not  be  -ve')
		    exit() #  How  to  stop  execution
class   rectangle(shape):
	def  get(self):
		print('Enter  length  and  breadth  of  rectangle')
		super() . get()  #  How  to  read  length  and  breadth
		self . b = float(input())
	def   area(self):
		return   self . a * self . b #  area  of  rectangle
	def   peri(self):
		return  2 * (self . a + self . b)  #   perimeter  of  triangle
	def  test(self):
		if  self . a  ==  self . b:   #  length  and   breadth  same
		    print('Not  a rectangle')
		    exit()  #  How  to  stop  execution
class   square(shape):
	def   get(self):
		print('Enter  any  side  of  square :  ' , end =  '\t')
		super() . get()  #  How  to  read  side
	def   area(self):
		return  self . a  **  2   #  area  of  square
	def   peri(self):
		return  4 * self . a   # perimeter  of  square
	def  test(self):
		pass
'''
1) Can  test()  method  be  omitted  from  square  class ?   --->  No

2) What  happens  when  test()  method  is  omitted  from  square  class ?  --->
													square  class  object  can  not  be  created  becoz  it  is  an  abstract  class  with
													inherited  abstract  method  test()
'''
def   menu():
	print('1. Triangle')
	print('2. Circle')
	print('3. Rectangle')
	print('4. Square')
	print('5. Exit')
# End  of  menu  function
def   operation(s):
	s . get()  #  How  to  read  inputs  to  object  's'
	s . test()  #  How  to  test  inputs  are  valid  (or)  not
	print('Area  :  ' ,  s . area())
	print('Perimeter  :  ' ,  s . peri());
# End  of  the  function
menu()
ch = eval(input('Enter  choice  :  '))  #  4
while  ch <  5:   #  repeat  until  user  input  is  5
	match   ch:
		case  1:
			operation(triangle())  #   How  to  call  operation()  function
		case  2:
			operation(circle())  #  How  to  call  operation()  function
		case  3:
			operation(rectangle())  #  How  to  call  operation()  function
		case  4:
			operation(square())  #  How  to  call  operation()  function
	#end  of  match
	menu()
	ch = int(input('Enter   choice  :  ')) #  5
# End of while  loop
print('Good  Bye')

'''
What  is  the  advantage  of  program ?  --->  Methods  are  multiple  but  call  is  same  for  all  of  them
'''