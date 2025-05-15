# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))  #  100  <next  line>   400  <next  line>   144 <next  line>  324 <next  line>  196  <next  line>
		time . sleep(1)
	except:
		break


'''
1) What  is  value  of  argument  'x'  in  lambda  function ?  --->  Each  element  of  list  'a'
    What  is  value  of  argument  'y'  in  lambda  function ?  --->  Each  element  of   map  object  i.e. x **  2

2) What  does  map  object  contain ?   --->  100 , 400 , 225 , 144 , 324, 25 , 196 , 625 , 289
    What  does  filter  object  contain ?   ---> 100 , 400 , 144 , 324, 196
'''