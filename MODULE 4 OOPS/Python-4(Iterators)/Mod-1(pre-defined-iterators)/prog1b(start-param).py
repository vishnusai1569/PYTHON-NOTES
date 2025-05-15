# Find  outputs (Home  work)
import   time
#        0       1         2          3
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except:
		break


'''
1) What  does  start = 5  do ?  --->   Enumerated  index  starts  from  5

2) What  happens  when  start = 5  is  omitted ?  --->  Default  start  is  0
'''