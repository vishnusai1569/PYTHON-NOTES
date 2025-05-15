

'''
Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  --->  2 / 3 + 5 / 9 =  (18 + 15) / 27 =  33 / 27 =  11 / 9
    What  is  the  difference  ?  ---> 2 / 3 - 5 / 9 = (18 - 15) / 27 = 	3 / 27 = 1 / 9
    What  is  the  product  ?  --->  2 / 3 * 5 / 9 =	10 / 27  = 10 / 27
    What  is   the  division  ?  --->  2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division  and   return  True

2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 = (18 + 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 = (18 - 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  product  ?  --->  2 / 3 * 0 / 9 =	0 / 27  =  0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  --->   2 / 3 /  0 / 9 =  2 / 3 * 9 / 0 =  18 / 0  ---> Division  is  not   permitted  and  return  False

3) When  is  simplification  required ?  ---> When  numerator  is  non-zero

4) What  does  div()  method  return ?  ---> True  when  division  is  succesful  and  False  otherwise
'''
import  math
class  rat:
	def  get(self):
		self . nr = int(input('Enter  numerator :  '))
		self . dr = int(input('Enter  denominator :  '))
		self . test()
	def  test(self):
		while  self . dr == 0:
			self . dr = int(input('Denom  can  not  be  zero , reenter :  '))
	def    __str__(self):
			 return  F'{self . nr} / {self . dr}'
	def   add(self , a , b):
		self . nr = a . nr * b . dr + a . dr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self . nr = a . nr * b . dr - a . dr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self . nr = a . nr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		self . nr = a . nr * b . dr
		self . dr = a . dr * b . nr
		self . simplify()
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
		if  self . nr != 0:
			ans = math . gcd(self . nr , self . dr)
			self . nr = self . nr // ans
			self . dr = self . dr // ans
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
if  __name__ == '__main__':
	a = rat()
	b = rat()
	c = rat()
	d = rat()
	e = rat()
	f = rat()
	a . get()
	b . get()
	c . add(a , b)
	d . sub(a , b)
	e . mul(a , b)
	f . div(a , b)
	print('Sum : ' , c)
	print('Difference : ' , d)
	print('Product : ' , e)
	if  b . nr != 0:
		print('Division : ' , f)
	else:
		print('Division  is  not  permitted')




'''
1) Can  a  method  call  another  method  of  same  class ?  --->  Yes  with  self . method()

2) get()  calls  which  method  ?  --->  Method  test()  of  the  same  class

3) If  get()  method  is  called  wrt  obj  'a' ,
    test()  method  is  called  wrt  which  object ?  ---> Same  object  'a'  due  to  self . test()

4) add()  calls  which  method  ?  ---> Method  simplify()  of  the  same  class

5) If  add()  method  is  called  wrt  object  'c',
     simplify()  method  is  called  wrt  which  object ?  --->  Same  object  'c'  due  to  self . simplify()
'''