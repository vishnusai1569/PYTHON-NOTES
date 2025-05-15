# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2))
while   True:
	try:
		print(next(m)) #   0  <next  line>   1   <next  line>  4   <next  line>  9   <next  line>  ...  81   <next  line>
		time . sleep(1)
	except:
		break


'''
1) Is  map(pow, range(10) , 2)  valid  ? --->  No  becoz  2  is  neither  iterable  nor  iterator

2) What  are  the  results  of  while  loop  when  it  is  map(pow , range(10) , range(2 , 3)) ?  --->
												0 ^ 2  and  StopIteration  error  is  raised  becoz   2nd  range  object  is  exhausted

3) What  are  the  results  of  while  loop  when  it  is  map(pow , range(10) , range(2)) ?  --->
											0 ^ 0 , 1 ^ 1   and  StopIteration   Error  is  raised  becoz   2nd  range  object  is  exhausted

4) What  are  the  results  of  while  loop  when  it  is  map(pow ,  repeat(2) , range(10)) ?  --->  2 ^ 0 , 2 ^ 1 , 2 ^ 2  ,  ....  2 ^ 9
'''