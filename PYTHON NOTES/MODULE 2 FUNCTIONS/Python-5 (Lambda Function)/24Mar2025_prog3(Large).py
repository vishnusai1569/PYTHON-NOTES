#  Find  outputs (Home  work)
large=lambda x,y :  max(x , y) #How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10  ,  20)) #   'x'  is  10 , 'y'  is  20  and  result  is  20
print(large(10.7  ,  5.6))  #   'x'  is  10.7 , 'y'  is   5.6  and  result  is   10.7
print(large('g'  ,  's'))  #   'x'  is    'g'  , 'y'  is   's'   and  result  is   's'
print(large('Rama'  ,  'Rajesh'))  #   'x'  is   'Rama'  , 'y'  is   'Rajesh'  and  result  is   Rama
print(large(True  ,  False))  #   'x'  is   True  , 'y'  is   False  and  result  is   True



'''
1) large  =  lambda   a  ,  b :   max(a , b)
    How  to  define  the  above  lambda  function  without  using  max()  function ?  --->
																									large = lambda  a , b :  a   if  a > b  else  b

2) large  =  lambda   x  ,  y :   if  x > y:  return  x  else:    return   y
    Is  the  above   statement  valid ? ---> No  becoz   lambda   function  can  not  use  if  and  return

3) In  other  words,   lambda  function  can  not  use  if , match ,  for  and  while

4) Can  lambda  function  use  ternary  operator  ?  ---> Yes
'''
