# Find  outputs (Home  work)
class c1:
    x = 10   # Adds  static  variable  'x'  to  class  c1  with  value  10
    def  __init__(self):
	    self . y = 20   # Adds  variable  'y'  to    object  self   with  value   20
a = c1()  #  Object  is  initialized  with  y = 20  by  constructor
b = c1()  #  Object  is  initialized  with  y = 20  by  constructor
a . x = 30    # Adds  variable  'x'  to    object   'a'   with  value   30
b . y = 40  #  Modifies  b . y  to  40
print(b . x)  # static  variable  as there  is  no  variable  'x'  in  object  'b'  i.e.  10
print(b . y)  #40
print(a . x)  #  30
print(a . y)  #  20
print(c1 . x)  #  10
print('Object a : ', a . __dict__) #   {'y' : 20 , 'x' : 30}
print('Object b : ', b . __dict__) #  {'y' : 40}
print(c1 . __dict__) #   {'x' :  10 , Ev's}

'''
static  variable   --->  x = 10

Object  'a'  --->  y = 20 ,  x = 30

Object  'b'  --->  y = 40
'''