#(Home  work)
#  Can  string  be  enumerated ?   --->  Yes
import   time
a = input('Enter  any  string  :  ') #  'Hyd'
e = enumerate(a)  #  Creates  an  empty  object
while   True:
	try:
		print(next(e))  #  (0 , 'H')  <next  line>  (1 , 'y')   <next  line>  (2 , 'd')   <next  line>
		time . sleep(1)
	except  StopIteration:
		break


'''
Is  next('Hyd')  valid ?  --->  No  becoz  next()  function  demands  sequence  but  'Hyd'   is  not  an  iterator
'''