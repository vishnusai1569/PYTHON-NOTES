# Find outputs
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
list = [10 , 0 ,  -25 , () , (25,) , 'Hyd', '' , [] , 10.8 , 0.0 , [10 , 20] , True , False]
f1 = filter(lambda  x : None  , list)  #  Creates  an  empty  filter  object
print('Filter  f1')
disp(f1)  #  'f'  is  object  f1  and  result  is  nothing
f2 = filter(None  , list)  #   Interpreted  as   f2 = filter(lambda  x : x , list)
print('Filter  f2')
disp(f2) #  'f'  is  object  f2  and  result  is   those  elements of  list  which  are  True  i.e.  10  <next  line>  -25  <next  line>  (25,) <next  line>   Hyd  <next  line>  10.8  <next  line>  [10,20]  <next  line>  True  <next  line>



'''
1) f1 = filter(lambda  x : None  , list)
    What  does  filter  do  when  lambda  function  returns  None ?   --->
																Picks  no  element  of  the  list  becoz  None  is  interpreted  as  False

2) How  is  filter(None , list)  interpreted ?  --->  filter(lambda  x : x , list)

3) filter(lambda  x : x , list)
    What  does  filter  do  when  lambda  function  returns   'x'  itself  ?   --->
																Picks  those  elements  of  the  list   which  are  interpreted  as  True  and
																ignores  remaining  elements
'''