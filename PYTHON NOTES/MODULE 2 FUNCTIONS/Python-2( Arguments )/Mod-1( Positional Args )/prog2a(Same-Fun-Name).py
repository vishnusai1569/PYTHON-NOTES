# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z): #  Recognized
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)
#f1(40 , 50)   #   Error  :  Arg  is  not  passed  for  'z'
#f1(60)   #   Error  :  Args   are  not  passed  for  'y'  and  'z'
#f1()  #   Error  :  Args  are   not  passed  for  'x' , 'y'  and  'z'



'''
1) Which  function  is  executed  when  functions  have  same  name ?  --->  Last  function

2) What  about  remaining  functions ?  --->  Discarded

3) When  is  a  function  discarded ?  --->  When  another  function  is  defined  with  same  name

4) There  is  no  function  overloading  in  python  (unlike  c++)
'''
