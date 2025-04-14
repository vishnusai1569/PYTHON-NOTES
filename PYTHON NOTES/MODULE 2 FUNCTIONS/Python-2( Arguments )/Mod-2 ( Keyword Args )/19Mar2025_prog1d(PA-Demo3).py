#  Gift
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))  #  23
print(f1(*[6 , 7 , 8]))#   62
#print(f1([6 , 7 , 8]))  #  Error: Args  are  not  passed  for  'b'  and  'c'
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))  #  16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))  #  14
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))   #  Error: Args  are  not  passed  for  'b'  and  'c'
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})  #    {'c' : 2 , 'b' :  4 , 'a' : 6}
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))  #  Error  :  Arg  'x'  does  not  exist


'''
1) What  does  f1(*[6 , 7 , 8])  do  ?  ---> Unpacks  list  to  three  elements  i.e.  6   7    8
																						and
																the  three  elements  are  copied  to  formal  parameters  a , b , c


2) What  is   the  issue  with  f1([6 , 7 , 8])  ?  --->
													'a'  is  [6 , 7 , 8]  and  error  becoz  arguments  are  not  passed  for  'b'  and  'c'

3) What  does  f1(*{1 : 2 , 3 : 4 , 5 : 6})  do ?  ---> Unpacks  dictionary  to  keys   1  , 3 ,  5
																										and
																			  the  three  keys  are  copied  to  formal  parameters  a , b , c

4) What  does  f1(**{'c' : 2 , 'b' : 4 , 'a' : 6}  do ?  ---> Unpacks  dictionary  to  keyword  args   i.e.  c = 2 , b = 4 , a = 6
																													and
																					  values  of  arguments  are  copied  to  formal  parameters  a , b  and  c

5) What  is  the  issue  with  f1({'c' : 2 , 'b' :  4 , 'a' : 6}) ?  --->
					'a'  is   {'c' : 2 , 'b' :  4 , 'a' : 6}  and  throws  error  becoz   arguments  are  not  passed   for  'b'  and  'c'
'''
