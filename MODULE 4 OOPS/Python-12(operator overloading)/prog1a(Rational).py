'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

1) First  rational  number  --->  2 / 3
   Second  rational  number ---> 5 / 9
   What  is  the  sum  ?  --->   2 / 3 + 5 / 9 =  (18 + 15) / 27 =  33 / 27 =  11 / 9
   What  is  the  difference  ?  ---> 2 / 3 - 5 / 9 =  (18 - 15) / 27 =  3 / 27 =  1 / 9
   What  is  the  product  ?  --->  2 / 3 * 5 / 9 =  10 / 27 =  10 / 27
   What  is   the  division  ?  --->   2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 = 18 / 15 = 6 / 5

2) First  rational  number  --->  2 / 3
   Second  rational  number ---> 0 / 9
   What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  difference  ?  --->  2 / 3 - 0 / 9 = (18 - 0) / 27 = 18 / 27 = 2 / 3
   What  is  the  product  ?  --->  2 / 3 * 0 / 9 =  0 / 27 = 0 / 27  (simplification  is  not  required  becoz  numerator  is  0)
    What  is   the  division  ?  --->  2 / 3 /  0 / 9 =  2 / 3 * 0 / 9  --->  Division  is  not  possible  becoz  b . nr  is  0

3) Modify  the  following  program  with  operator  overloding  methods

4) Leave  get() ,  test() , __str__()  and  simplify()  methods  unchanged
'''
import  math
class  Rat:
	def  get(self):
		self . nr = int(input('Enter  numerator : '))
		self . dr = int(input('Enter  denominator : '))
		self . test()
	def  test(self):
		while  self . dr == 0:
			self . dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))
	def    __str__(self):
		return  F'{self . nr} / {self . dr}'
	def  __add__(a , b):
		c = Rat()  #  Creates  local  object
		c . nr = a . nr * b . dr + a . dr * b . nr #  Adds  rational  numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
		c . dr = a . dr * b . dr
		c . simplify()  # Simplifies  rational  number  in  object  'c'
		return   c   #  Returns  object  before  it  is  lost
	def  __sub__(a , b):
		c = Rat()  #  Creates  local  object
		c . nr = a . nr * b . dr - a . dr * b . nr  #  Subtracts  rational  numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
		c . dr = a . dr * b . dr
		c . simplify()  # Simplifies  rational  number  in  object  'c'
		return  c   #  Returns  object  before  it  is  lost
	def  __mul__(a , b):
		c = Rat()  #  Creates  local  object
		c . nr = a . nr * b . nr   #  Multiplies  rational  numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
		c . dr = a . dr * b . dr
		c . simplify()  # Simplifies  rational  number  in  object  'c'
		return  c   #  Returns  object  before  it  is  lost
	def  __truediv__(a , b):
		c = Rat()  #  Creates  local  object
		c . nr = a . nr * b . dr   #  Divides  rational  numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
		c . dr = a . dr * b . nr
		c . simplify()  # Simplifies  rational  number  in  object  'c'
		return  c   #  Returns  object  before  it  is  lost
	def   simplify(self):
		if self . nr != 0:
			g = math . gcd(self . nr, self . dr)
			self . nr = self . nr // g
			self . dr = self . dr // g
# End  of  the  class
a = Rat()   #  Creates  2  empty   objects
b = Rat()
a . get()  #  Reads  numerator  and  denominator  into  object  'a'
b . get()   #  Reads  numerator  and  denominator  into  object  'b'
print('Sum :  ' , a + b)  #  Executes   __add__()  and  __str__()   methods  of  class  Rat
print('Difference :  ' , a - b) #  Executes   __sub__()  and  __str__()   methods  of  class  Rat
print('Product :  ' ,  a * b)  #  Executes   __mul__()  and  __str__()   methods  of  class  Rat
if b . nr != 0:
	print('Division  : ' , a / b)  #  Executes   __truediv__()  and  __str__()   methods  of  class  Rat
else:
	print('Division is not permitted.')



'''
1) return   object
    What  is  returned  (id  of  the  object (or)  values  of  the  object) ?  --->  Values  of  the  object

2) Are  get() , test()  and  simplify()  operator  overloading  methods ?  --->  No  and  they  are  regular  methods

3) Is  __str__()  an  operator  overloading  method ?  --->
								No  and  it  is  a  special  method  which  is  automatically  executed  as  soon  as  object  is  printed

4) What  are  __add__() , __sub__() , __mul__()  and  __truediv__()  called ?  --->  Operator  overloading  methods

5) print(a + b)
    How  many  methods  are  executed  ?  --->  Two  i.e.  __add__()  and  __str__()

6) class   c1:
	   def  __add__(a , b):
			print(10 + 20)
    Is  10 + 20  a  recursion ?  --->  No  becoz  10  and  20  are  integers  but  not  c1  class  objects

7) class   c1:
	   def  __add__(a , b):
		      x = c1()
		      y = c1()
			print(x + y)
    Is  x + y   recursion ?  --->  Yes  becoz  x  and  y  are  c1  class  objects
'''