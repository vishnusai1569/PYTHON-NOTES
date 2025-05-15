#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self . a = int(input('Enter a Number : '))  # How  to   read  inputs  into   variables  a  and  b  of  object  self
		self . b = int(input('Enter a Number : '))
	def    disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')	# How  to  print  variables  a  and  b  of  object  self  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		super() . get() # How  to   read  inputs  into   variables  a  and  b  of  object  self
		self . c = int(input('Enter a Number : '))  #  # How  to   read  inputs  into   variables  c  and  d  of  object  self
		self . d = int(input('Enter a Number : '))
	def   disp(self):
		super() . disp()  #  How  to  print  variables  a  and  b  of  object  self  in  same  line  separated  by  tab
		print(self . c , self . d , sep = '\t') # How  to  print  variables  c  and  d  of  object  self  in  same  line  separated  by  tab
	def  total(self):
		return self . a + self . b + self . c + self . d # sum  of  values  in  object  self
# End of child class
print('parent  object')
p = parent()
p . get()  # How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
c = child()
c . get()   # How  to  read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
p . disp() # How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c . disp() # How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' , c . total()) # How  to  obtain  sum of  values  of  object  'c'



'''
object  p  --->  a = 10 , b = 20

object  c  ---> a = 30 , b = 40 , c = 50 , d = 60
'''


'''
1) How  many  methods  are  executed  internally  for  c . get() ?  ---> Two  methods
																                                              i.e.  parent  class   get()  and  child  class  get()

2) What  does  parent  class  get()  method  do ?  --->  Reads  instance  variables  a  and  b
     What  does  child  class  get()  method  do ?  --->  Reads  instance  variables  a , b ,  c  and  d

3) Which  class  methods  are  executed  for  super() . get()  and  super() . disp() ?  --->
																				parent  class   methods  becoz  super()  refers  to  parent  class

4) super() . get()
    Wrt   which  object  is  parent  class  get()  method  called  ?  --->
																					Object  'c'  becoz  child  method  is  called  wrt  object  'c' and
																					hence  parent  method  is  also  called  wrt  same  object

5) How  many  methods  are  executed  internally  for  c . disp() ?  --->  Two  methods
																		                                        i.e. parent  class   disp()  and  child  class  disp()

6) What  does  parent  class  disp()  method  do ?  --->  Prints  instance  variables  a  and  b
     What  does  child  class  disp()  method  do ?  --->  Prints  instance  variables  a  , b  , c  and  d
'''