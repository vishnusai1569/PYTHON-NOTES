# Write  a   program  to  square  each  element  of  list  with  map  iterator
import  time
a = [10 , 20 , 15 , 18 , 5]
m = map(lambda  x :  x * x  ,  a) #  Empty  object
print(type(m))  #  <class  'map'>
print(m) #   Type  and  address  of   object  'm'
while   True:
	try:
		print(next(m))  #  100  <next  line>  400  <next  line>  225  <next  line>  324  <next  line>   25  <next  line>
		time . sleep(1)
	except:
		break