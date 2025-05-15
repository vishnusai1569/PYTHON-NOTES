# Find  outputs (Home  work)
import  time
a = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   a) #  Creates  an  empty  filter  object
while  True:
	try:
		print(next(f))  #   25  <next  line>  10.8  <next  line>  3+4j  <next  line> Hyd  <next  line>  False  <next  line>
		time . sleep(1)
	except:
		break



'''
1) What  is  the  value  of  'x'  in  lambda  function ?  --->  Each  element  of  list  'a'

2) a = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
    f = filter(lambda   x :   True ,   a)
    How  many  times  is  lambda  function  executed ?  ---> 5  times  becoz  there  are  5  elements  in  list  'a'
    How  many  times  is  while  loop  executed ?  ---> 5 + 1 = 6  times

3) f = filter(lambda   x :   True ,   a)
    What  does  filter  do  when  lambda  function  returns  always  True ?  --->   Picks  every  element  of  the  list

4) How  to  define  regular  function  instead  of  lambda  function ? --->  def   f1(x):
																													      return  True

5) How  to  modify  filter  with  regular  function ?  --->  f = filter(f1 , a)
'''