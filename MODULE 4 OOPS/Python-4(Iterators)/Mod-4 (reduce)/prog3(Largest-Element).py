'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  --->  40

Hint:  Use  reduce()  function
'''
from  functools  import  reduce
list = eval(input("Enter list of numbers (or) strings:"))
ans = reduce(lambda  x , y :   max(x , y) , list)
print('Largest  element  :   '  ,  ans)


'''
    x       y         max(x , y)
------------------------------
  10      20             20
  20      15             20
  20      30             30
  30      25             30
  30      40             40
  40      35             40
---------------------------------
What  is  the  alternative  to  max(x , y) ?  --->  x  if  x > y  else  y
'''