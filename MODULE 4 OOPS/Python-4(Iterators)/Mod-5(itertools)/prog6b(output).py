#  Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object')
while   True:
	try:
		print(next(r))  #  25   <next  line>  25  <
		time . sleep(1)
	except:
		break
print('2nd  repeat  object')
r  =  repeat('Hyd')
while   True:
	print(next(r))
	time . sleep(1)


'''
1st  repeat  object
25
25
25

2nd  repeat  object
Hyd
Hyd
Hyd
upto infinite times
'''


'''
Why  are  try  and  except  not  used  in  the  2nd  while  loop ?  --->
													Since  repeat  is  an  infinite  iterator  as  times  argument  is  missing
													and  hence  StopIteration  error  is  never  raised
'''