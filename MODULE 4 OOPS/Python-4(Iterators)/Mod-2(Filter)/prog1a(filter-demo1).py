# filter  iterator  demo  program
import  time
a = [25 , 9 , 10 , 15 ,  17 , 24 , 35 , 47 , 0 , 19 , 53 , 18 , 65 , 83]
f = filter(lambda  x :  x % 2 == 0  , a)  #  Empty  filter  object
print(type(f))  #   <class  'filter'>
print(f)  #  Type  and  address   of   object  'f'
while   True:
	try:
		print(next(f))  #  10  <next  line>   24  <next  line>  0  <next  line>   18  <next  line>
		time . sleep(1)
	except  StopIteration:
		break






'''
1) How  many  times  is  lambda  function  executed  ?  --->  len(a)  times
                                                                                             i.e.  14  times  becoz  there  are  14  elements  in  list  'a'

2) In  other  words,  lambda  function  is  executed  on  each  element  of  list  'a'

3) How  many  times  is  while  loop  executed ?  --->  4 + 1 = 5  times  becoz  lambda  function  returns  True  4  times

4) What  happens  when  lambda  function  returns  True  ?  --->  'x'  is  returned   to  next(f)
    What  happens  when  lambda  function  returns  False  ?  --->  Ignores  'x'  and  moves  to  next  element  of  list  'a'

5) f = filter(lambda  x :  x % 2 == 0  , a)
    Finally  filter  iterator  selects  even  numbers  of  the  list  and  ignores  odd  numbers
'''