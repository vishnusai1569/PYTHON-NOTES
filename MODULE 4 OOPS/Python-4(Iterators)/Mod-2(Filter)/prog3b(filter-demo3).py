#  Find  outputs (Home  work)
import  time
a = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  a) #  Creates  an  empty  filter  object
while  True:
	try:
		print(next(f))  #   Throws  StopIteration  error  in  1st  iteration  itself
		time . sleep(1)
	except:
		break


'''
1) What  is  the  value  of  'x'  in  lambda  function ?  ---> Each  element  of  list  'a'

2) a = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
    f = filter(lambda   x :   False ,   a)
    How  many  times  is  lambda  function  executed ?  ---> 5  times  becoz  there  are  5  elements  in  list  'a'
    How  many  times  is  while  loop  executed ?  --->  Just  once

3) f = filter(lambda   x :  False ,   a)
    What  does  filter  do  when  lambda  function  returns  always  False ?  --->   Picks  no  element  of  list  'a'
'''