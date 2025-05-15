# Find  outputs (Home  work)
import  time
a = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda   x   :   x   ,   a) #  Creates  an  empty  filter  object
while  True:
	try:
		print(next(f))  #  25  <next  line>   10.8  <next  line>  3+4j  <next  line>  Hyd  <next  line>  (25,)  <next  line>
		time . sleep(1)
	except:
		break


'''
     x                          return   x										next(f)
-----------------------------------------------------------------------------------------------------
    25              25  is  Non-zero i.e. True								25
    10.8            10.8  is  Non-zero i.e. True							10.8
    False           False															     ----
    3 + 4j          3 + 4j  is  True												3 + 4j
    0                 0  is  False													     -----
    'Hyd'          'Hyd'  is  non-empty  string  i.e. True	  		Hyd
    ''                ''  is  False													     ----
    (25,)           (25,)  is  non-empty tuple  i.e.  True  			   (25,)
    ()		          ()  is  empty tuple i.e.  False						    ----


1) How  many  times  is  lambda  function  executed ?  --->  9  times  becoz  there  are  nine  elements  in  the  list

2) How  many  times  is  while  loop   executed ?  ---> 5  + 1  = 6  times
'''