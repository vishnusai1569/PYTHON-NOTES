# Design  an  iterator  which  yields   1 , 2 , 3
import  time
class   c1:
	def  __init__(self):  #  self  is   object  itr
		self . x = 0   #  Adds  variable  'x'  to  object  itr  with  value  0
	def  __next__(self):  #  self  is  object itr
		self . x += 1  #   5
		if  self . x <= 3:
				print('__next__  method ')
				return  self . x
		raise  StopIteration
# End  of  the  class
itr  =  c1() #   Object  is  initialized  with  x = 0  by  constructor
while  True:  #  Iteration  4
	try:
		print(next(itr))  #  3
		time . sleep(1)
	except:
		break
#  End  of  while  loop
'''
for  y  in  itr:  #  Error :  No  __iter__()  method  in  class  c1
	print(y)
'''



'''
1) Can  __next__()  method  raise  any  other  error ?  ---> Yes

2) What  happens  when  __next__()  method  does  not  raise  any  error  ?  --->
														It  returns  None  by  default  from  4th  iteration  and  c1  becomes  an  infinite  iterator
    What  are  the  outputs ?  --->
									__next__  method  ,  1 ,  __next__  method  ,  2 , 	__next__  method  , 3 , None , None , None , .......

3) What  happens  when   if  condition  is  omitted  from  __next__()  method  ?  --->  c1  becomes  an  infinite  iterator
     What  are  the  outputs ?  --->
				__next__  method  ,  1 ,  __next__  method  ,  2 , 	__next__  method  , 3 ,  __next__  method ,  4  and  so  on
'''