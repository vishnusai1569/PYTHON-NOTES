 #Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y  #   Ref  add  points  to  outer  lambda  function
a = add()  #  'x'  is  default  value  and  a =  lambda   y : 10 + y  --->  Ref  'a'  points  to  inner  lambda  function
print(a(20)) #   'y'  is  20  and  result  is  10 + 20 = 30
print(add(30)(40)) #  (lambda  y :  30 + y)(40)  =  70


'''
1) Where  does  reference  add  point  to  ?  --->  outer  lambda  function

2) What  is  executed  for  add() ?  --->  outer  lambda  function  with  default  value  10

3) What  does  add()  return ?  --->  Inner  lambda  function
													     i.e.  lambda   y : 10 +  y

4) Where  does  reference  'a'  point  to  ?  --->  Inner  lambda  function

5) What  is  executed  for  a(20) ?  --->  inner  lambda  function  with  y = 20

6) How  many  lambda  functions  are  executed  for  add(30)(40) ?  --->  Two

7) What  does  add(30)  return ?  --->  Inner  lambda  function
															  i.e.  lambda  y : 30 + y
'''
