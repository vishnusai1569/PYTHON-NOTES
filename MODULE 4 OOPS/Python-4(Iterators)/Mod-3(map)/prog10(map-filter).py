# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m))  #   40  <next  line>  30 <next  line>  36 <next  line>   50 <next  line>   34 <next  line>
		time . sleep(1)
	except:
		break


'''
1) What  is  value  of  argument  'x'  in  lambda  function ?  --->  Each  element  of  list  'a'
    What  is  value  of  argument  'y'  in  lambda  function ?  --->  That  element  of   list  'a'  which  is  picked  by  filter

2) What  does  filter  object  contain ? --->  20 , 15 , 18 , 25 , 17
     What  does  map  object  contain ? --->   40 ,  30 ,  36 , 50 , 34

3) Where  is  y + y   returned  to  ?  --->  next(m)
'''
