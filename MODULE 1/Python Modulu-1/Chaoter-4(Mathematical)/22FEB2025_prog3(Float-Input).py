# How  to  read  float  input ?  --->  float(input())
try:
	x = float(input('Enter  float  number  :  ')) #   Reads  string  input  and  converts  to  float
	print(type(x)) #  <class  'float'>
	print(x) #  User  input
except: #  Executed  when  there  is  an  error
	print('Input  should  be  float  (or)  integer')


'''
Input     What  does  input()   read      What  does  float(input())  return
---------------------------------------------------------------------------------------
 10.8                        '10.8'                                float('10.8')  is  10.8
 25						   '25'                                  float('25')  is  25.0
 3+4j					   '3+4j'                               float('3+4j')  throws  error
 True					   'True'                               float('True')  throws  error
-----------------------------------------------------------------------------------------
1) What  is  the  result  of  float(True)  ?  ---> 1.0

2)What  is  the  result  of  float('True')  ?  --->  Error
'''
