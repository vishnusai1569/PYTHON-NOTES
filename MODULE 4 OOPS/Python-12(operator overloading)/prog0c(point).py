'''
Overload  +  operator  on  point  class  objects

What  does  point  class  object  contain ?  --->  x , y
'''
class  point:
	def  get(self):
		self . x = float(input('Enter  value  of  x  co-ordinate  :  '))
		self . y = float(input('Enter  value  of  y  co-ordinate  :  '))
	def  __add__(self , b):
		d = point()
		d . x = self . x + b . x
		d . y = self . y + b . y
		return  d
	def  __str__(self):
			return  F'({self . x} , {self . y})'
#  End  of  the  class
a = point()  #  Creates  3  empty  objects
b = point()
c = point()
print('1st  point')
a . get()
print('2nd  point')
b . get()
print('3rd  point')
c . get()
print('Sum  of  the  2  points :  ' ,  a + b + c)


'''
Object  'a'   --->  x  =3 , y = 4

Object  'b'   --->  x = 5 , y = 6

Object  'c'   --->  x = 7 , y = 8

1) How  many  method  calls  are  in  a + b + c ?  --->  Two

2) What  is  the  first  method  call ?  ---> a + b
     What  is  the  2nd  method  call ?  --->   _ + c

3) Where  are  results  of  a + b  stored ?  --->  In  1st  nameless  object
     Where  are  the  results  of  a + b +  c  stored ?  --->  In  2nd  nameless  object
'''