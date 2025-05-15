'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without
using  pre-defined  complex  object

First  complex  number  --->  3 + 4i
Second  complex  number ---> 5 + 6i
What  is  the  sum  ?  --->   8 + 10i
What  is  the  difference  ?  --->  -2 - 2i
What  is  the  product  ?  ---> (3 + 4i) * (5 + 6i) =   15 + 18i + 20i - 24 =   -9 + 38i
What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =   (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =
 											     =  (15 - 18i + 20i + 24) / (25 + 36) =  39 / 61 + 2i / 61
'''
import  math
class  complex:
	def  get(self):
		self . real = float(input('Enter  real  part :  '))  #  How  to  read  real  and  imag  into  object  self
		self . imag = float(input('Enter  imag  part :  '))
	def    __str__(self):
		if  self . imag > 0:
			return  F'{self.real}  +  {self.imag} i'  #  How  to  return  real  and  imag  in  the  form  of  3 + 4i
		else:
			return  F'{self.real}  -  {-self.imag} i'  #  How  to  return  real  and  imag  in  the  form  of  3 - 4i
	def  __add__(a ,  b):  #  How  to  add  objects  self ,  b  and  store  the  results  in  a  local  object  and  finally  return  local  object
		c = complex()  #   Creates  a  local  object
		c . real = a . real + b . real  #  Adds  complex  numbers  in  objects  'a'  and 'b'  and  stores  result  in  object 'c'
		c . imag = a . imag + b . imag
		return  c   # Returns  object  before  it  is  lost
	def  __sub__(a  ,  b):   #  How  to  subtract  objects  self ,  b  and  store  the  results  in  a  local  object   and  finally  return  local  object
		c = complex()  #   Creates  a  local  object
		c . real = a . real - b . real   #  Subtracts  complex  numbers  in  objects  'a'  and 'b'  and  stores  result  in  object 'c'
		c . imag = a . imag - b . imag
		return  c  # Returns  object  before  it  is  lost
	def  __mul__(a ,  b):  #  How  to  multiply  objects  self ,  b  and  store  the  results  in  a  local  object 	and  finally  return  local  object
		c = complex()  #   Creates  a  local  object
		c . real = a . real * b . real - a .imag * b . imag   #  Multiplies  complex  numbers  in  objects  'a'  and 'b'  and  stores  result  in  object 'c'
		c . imag = a . imag * b .  real +  a . real * b . imag
		return  c  # Returns  object  before  it  is  lost
	def  __truediv__(a,  b): #  How  to  divide  objects  self ,  b  and  store  the  results  in  a  local  object  	and  finally  return  local  object
		c = complex()  #   Creates  a  local  object
		c . real = (a . real * b . real + a .imag * b . imag) / (b . real ** 2 + b . imag ** 2)   #  Dividess  complex  numbers  in  objects  'a'  and 'b'  and  stores  result  in  object 'c'
		c . imag = (a . imag * b .  real -  a . real * b . imag) / (b . real ** 2 + b . imag ** 2)
		return  c # Returns  object  before  it  is  lost
# End  of  the  class
a = complex()  #  How  to  create  two  complex  class  objects
b = complex()
a . get()  #  How  to  read   inputs  into  1st  object
b . get()   # How  to  read   inputs  into  2nd  object
print('Sum :  ' , a + b)  #  Executes  __add__()   and  __str__()  methods   of  complex  class
print('Difference :  ' , a - b)   #  Executes  __sub__()   and  __str__()  methods   of  complex  class
print('Product :  ' ,  a * b)   #  Executes  __mul__()   and  __str__()  methods   of  complex  class
print('Division  : ' , a / b)   #  Executes  __truediv__()   and  __str__()  methods   of  complex  class