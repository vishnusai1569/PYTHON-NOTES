# Find  outputs (Home  work)
class c1:
    x = 10  #  'x'  is  global  to all  c1  class  objects
    def __init__(self):
	    self . y = 20
a = c1() #  Object  is  initialized  with  y = 20   by  constructor
b = c1()  #  Object  is  initialized  with  y = 20   by  constructor
a . x += 1 #  a . x = a . x + 1  --->  a . x  = 10 + 1 = 11  i.e.  Adds  variable  'x'  to  object  'a'  with  value  11
b . y += 1 #  Increments  b . y  by   1
print(a . x) #  Variable  'x'  of  object  'a'  i.e.  11
print(a . y)   #  Variable  'y'  of  object  'a'  i.e. 20
print(b . x) #   static  variable  becoz  there  is  no  b . x  i.e.  10
print(b . y)  #  Variable  'y'  of  object  'b'  i.e. 21
print(c1 . x) #   static  variable  'x'  of  class  c1   i.e. 10
print(a . __dict__) # {'y' : 20 , 'x' : 11}
print(b . __dict__) # {'y' : 21}
print(c1 . __dict__) # {'x' : 10 , Ev's}


'''
11
20
10
21
10
{'y': 20, 'x': 11}
{'y': 21}
{'x': 10,  Ev's}


static   variable  --->   x = 10

Object  'a'  --->  y = 20 ,  x  =  11

Object  'b'  --->  y = 21




1) What  is  the  expansion  for  a . x += 1  ? --->  a . x = a . x + 1

2) Which  variable  is  accessed  for  a . x  on  right  side ?  --->  Static  variable  becoz  there  is  no  variable  'x'  in  object  'a'

3) What  does  a . x  on  left  side  do ?  --->  Adds  variable  'x'  to  object   'a'  becoz  there  is  no  'x'  in  object  'a'
'''