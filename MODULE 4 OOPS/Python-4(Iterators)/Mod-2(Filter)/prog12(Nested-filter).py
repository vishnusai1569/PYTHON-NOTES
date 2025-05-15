# Nested  filter  i.e.  filter  on  filter
import   time
list =  [ (10 , 'Rama' , 10000.0) ,
            (20, 'Sita' , 7000.0) ,
            (15 , 'Rajesh' , 15000.0) ,
            (5 , 'Amar' ,  12000.0) ,
            (18 , 'Ramesh' , 8000.0) ]
f = filter(lambda  x :  x[1] . startswith('R')  , filter(lambda  x :  x[2] >= 10000 , list))
while   True:
	try:
		print(next(f))
		time .  sleep(1)
	except:
		break

'''
(10 , 'Rama' , 10000.0)
(15 , 'Rajesh' , 15000.0)
'''


'''
1) Which  filter  is  executed  first ?  --->  Inner  filter  is  executed  before  outer  filter

2) Which  tuples  are  yielded  by  next(f) ?  --->  Those  tuples  where  3rd  element  of  each  inner  tuple
													                           is  >=  10000  and  2nd  element  starts   with  'R'

3) What  is  'x'  of  inner  filter  ?  ---> Each  tuple  of  the  list
    What  is  'x'   of   outer   filter  ?  --->  That  tuple  which  is  picked  by  inner  filter
'''