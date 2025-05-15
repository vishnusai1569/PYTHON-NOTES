# getter  and  setter  methods  demo  program
class  Celsius:
	def   _init_(self , x):
		self . temp = x  #   setter   method  copies  37  to  a . _temp
	@property
	def  temp(self):  #  self  is   object  'a'
		print('Getter  method')
		return  self . _temp
	@temp . setter
	def   temp(self ,  y):  #  self  is   object  'a'  and  'y'  is  37
		print('Setter  method')
		if  y  <  -273.15:
			raise  ValueError('Temperature  below  -273  is  not  possible')
		self . _temp =  y   #  a . _temp =   37
	def   convert(self):   #  slef  is   object   'a'
		return   1.8 * self . temp  +  32  #   getter  method  returns   a . _temp  i.e.   37
#End  of  the  class
try:
	a  =  Celsius(37)  #  Constructor  adds   2  varibles  temp  =  37  and  _temp  = 37
	print(a . temp)  #   getter  method  returns   a . _temp  i.e.   37
	print('Farenheit  eqv  :  ' , a . convert())
	b  =  Celsius(-300)
	print('Hello')
except  ValueError  as  msg:
	print(msg)
print('End')


'''
Object  'a'   --->   temp = 37 , _temp = 37

Object  'b'  --->     temp = -300



1) What  happens  when  self . _temp = x  is  omitted  from  setter  method ? --->
														getter  method  throws  error  becoz  there  is  no  variable  _temp  in  object  self

2) Hence  self . _temp = x  is  mandatory  in  view  of  getter  method

3) What  is  the  issue  with  self . temp = x  in  setter  method ?  --->
																							Executes  same  setter  method  and  leads  to  recursion

4) What  does  a . temp = 37  do ?  --->  Assigns  37  to  a . temp  and  also  to  a . _temp  due  to  setter  method

5) What  is  the  issue  with  return  self . temp  in  getter  method ?  --->
																							Executes  same  getter  method  and  leads  to  recursion

6) What  happens  when  return  statement  is  omitted  from  getter  method ?  --->  None  is  returned  by  default

7) Where  is  None  returned  to  ?  --->   obj . temp
'''