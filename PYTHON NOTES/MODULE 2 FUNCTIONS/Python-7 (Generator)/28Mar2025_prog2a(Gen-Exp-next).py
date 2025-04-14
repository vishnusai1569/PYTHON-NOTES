#  How  to  define  generator  thru  expression
import  time
g = (x * x   for  x  in  range(5)) #   Creates  an  empty  gen  object
print(type(g))  #  <class  'generator'>
print(g) #  Type  and  address of  object 'g'
while   True:
	try:
		print(next(g))  #  0
		time . sleep(1)
		print('Hello')  #  Hello
	except   StopIteration:
		break
# End  of  while  loop
print('End')
#print(next(g)) #  StopIteration  error


'''
g = [x * x   for  x  in  range(5)]
------------------------------------
1) What  is  type(g) ?  ---> <class  'list'>

2) What  does  print(g)  do ?  --->  [0 , 1 , 4 , 9 , 16]

3) Is  next(g)  valid ?  --->  No  becoz  'g'  is  not  a  generator
'''
