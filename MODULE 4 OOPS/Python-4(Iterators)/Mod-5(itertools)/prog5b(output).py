#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c)) #  <class 'itertools.cycle'>
while   True:
	print(next(c))  #   10  <next  line>  20  <next  line>  30  <next  line>  40 <next  line>  10 <next  line>  20  <next  line>  30  <next  line>  40  <next  line>  10 <next  line>  and  so  on
	time . sleep(1)


'''
Why  are  try  and  except  not  used  in  the  above  program ?  --->
											Since  cycle  is  an  infinite  iterator  and  hence  StopIteration  error  is  never  thrown
'''