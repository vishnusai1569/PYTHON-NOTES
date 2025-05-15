#  Write  a  progran  to  add  num  class  objects  and  join  str  class  objects
from  abc  import  abstractmethod , ABC
class   datatype(ABC):
	@abstractmethod
	def  get(self):
		pass
	@abstractmethod
	def  add(self , m ,  n):
		pass
	@abstractmethod
	def  display(self):
		pass
'''
Who  should  implement  get() , add()  and  display()  methods ?  --->  Every  child  class  of  datatype
'''
class   number(datatype):
	def  get(self):
			self . x = eval(input('Enter a number: ')) # How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
	    self . x = m . x + n . x # How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
		print('Sum : ' , self . x) # How  to  print  sum  result
class   string(datatype):
	def  get(self):
		 self . x = input('Enter a string: ') # How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
	     self . x = m . x + n . x # How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
		 print('Join : ' , self . x) # How  to  print  sum  result
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
if  __name__  ==  '__main__':
	menu()
	ch =  eval(input('Enter choice : '))
	while  ch < 3: # Repeat   until  user  input  is  3
			if   ch == 1:
				a = [number() , number() , number()] # How  to  create  list  of  3  number  class  objects
			else:
				a = [string() , string() , string()] # How  to  create  list  of  3  string  class  objects
			a[0] . get() # How  to  read  input  into  first  object
			a[1] . get() # How  to  read  input  into  2nd  object
			a[2] . add(a[0] , a[1]) # How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
			a[2] . display() # How  to  print  3rd  object
			menu()
			ch = eval(input('Enter  choice : '))
		# end of  while  loop
	print('Good  Bye')


'''
1) Which  method  is  executed  for  x . method()  ?  --->
															number  class  method  is  executed  if  'x'  is   number  class  object   and
															string  class  method  is  executed  if  'x   is  a  string  class  object

2) What  is  the  key  to  execute  a  method  ?  --->  Type  of  object
'''