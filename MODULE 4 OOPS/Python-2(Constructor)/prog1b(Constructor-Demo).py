# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a  = Rat()  #  Object  is  initialized  with  nr = 22 , dr = 7  by  constructor
b = Rat(9)   #  Object  is  initialized  with  nr = 9 , dr = 7  by  constructor
c = Rat(5,  8)   #  Object  is  initialized  with  nr = 5 , dr = 8  by  constructor
d = Rat(dr1 = 9)    #  Object  is  initialized  with  nr = 22 , dr = 9  by  constructor
e = Rat(dr1 = 3 , nr1 = 2)    #  Object  is  initialized  with  nr = 2 , dr = 3  by  constructor
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is  11
y = eval(input('Enter Denominator  :  '))   #  Assume  that  input  is  15
f = Rat(x , y)  #  Object  is  initialized  with  nr = 11 , dr = 15  by  constructor
print('a  :  ' , a)  #   __str__()  method  returns   22 / 7  i.e.  a : 22 / 7
print('b  :  ' , b)   #   __str__()  method  returns   9 / 7  i.e.  b : 9 / 7
print('c  :  ' , c)   #   __str__()  method  returns   5 / 8  i.e.  c : 5 / 8
print('d  :  ' , d)   #   __str__()  method  returns   22 / 9  i.e.  d : 22 / 9
print('e  :  ' , e)   #   __str__()  method  returns   2 / 3  i.e.  e : 2 / 3
print('f  :  ' , f)   #   __str__()  method  returns   11 / 15  i.e.  f :  11 / 15
c . __init__()  #  Object  'c'  is  modified  to  nr = 22 , dr = 7  by  constructor
print('c  :  ' , c)   #   __str__()  method  returns   22 / 7  i.e.  c : 22 / 7
e . __init__(3.8  , 4.6)  #  Object  'e'  is  modified  to  nr = 3.8 , dr = 4.6  by  constructor
print('e  :  ' , e)   #   __str__()  method  returns   3.8 / 4.6  i.e.  e :  3.8 / 4.6
#g = Rat(nr1 = 9 , 5)  #  Error : PA  5  is  not  permittd  after  KA  nr1 = 9
#h = Rat(nr = 9 , dr = 5) #  Error :  No  args  nr  and  dr  for  constructor



'''
1) What is  the  advantage  with  default  arguments  to  constructor ?  --->  Object  can  be  created  with  0 , 1  (or)  2  arguments
																														Eg: Rat()  , Rat(5)  and  Rat(5 , 8)  are  valid
																															  due  to  default  arguments

2) What  is  the  issue  if  there  are  no  default  arguements  ?  --->  Object  has  be  created  with   two  arguments  only
																											   Eg:  Rat(5 , 8)

3) In  other  words,  Rat()  and  Rat(5)  throw  error  when  there  are  no  default  arguments

4) Can  argument  and  instance  variable  have  same  name ?  --->  Yes  but  not  recommended

5) How  are  they  distinguished  when  they  have  same  name ?  --->  Instance  variables  are  denoted  by  self . nr , self . dr
																		                                       and  parameters  are  denoted  by  nr , dr
																											   Eg:  def   __init__(self , nr = 22 , dr = 7):
																																self . nr = nr
																																self . dr = nr
'''