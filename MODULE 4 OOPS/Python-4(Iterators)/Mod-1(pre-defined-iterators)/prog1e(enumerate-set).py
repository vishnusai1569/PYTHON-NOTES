#  Can  set  be  enumerated  ?  (Home  work)
import  time
a = {25 , 10.8 , 'Hyd' , True}
print(a) #   {'Hyd' , 25 , True , 10.8}   in  any  order
b = enumerate(a)
while   True:
	try:
		print(next(b))  #  (0 , Hyd)  <next  line>  (1 , 25)  <next  line>  (2 , True) <next line>  (3 , 10.8)  <next  line>
		time . sleep(1)
	except  StopIteration:
		break


'''
1) Can  set  be  enumerated  ?  --->  Yes  even  though  it  is  not  indexed

2) How  are  indexes  yielded  when  set  is  not  indexed ?  --->  They  are  enumerated  indexes   but  not  set  indexes

3) Is  next(set)  valid ?  --->  No  becoz  set  is  not  an  iterator

4) Set  is   enumerated  in  the  same  order  in  which  it  is  printed  becoz  it  is   the  same  set
'''