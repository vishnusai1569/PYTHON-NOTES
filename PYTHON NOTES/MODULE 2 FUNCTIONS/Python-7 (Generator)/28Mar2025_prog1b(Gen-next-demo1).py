#  Style 1  : Defining  generator  through  function
import   time
def   f1(): #  Generator  function  due  to  yield
	print('One')
	yield   25
	print('Two')
	yield  10.8
	print('Three')
	yield   [10,20,15,18]
	print('Four')
# End  of  generator
g = f1()  #  Creates  an  empty  generator  object
print(type(g))  #  <class  'generator'>
print(g) #  Type  and  address  of  object  'g'
print(type(f1))#  <class  'function'>
while  True: #   Iteration  4
	try:
		print(next(g))  # 25  , 10.8 , Hyd
		time . sleep(1)
		print('Hello')
	except  StopIteration:
		break
#  End  of  while  loop
print('End')
#print(len(g))  #  Error  :  'g'  is not  a sequence
#print(next(g))  #  Throws  StopIteration  Error



'''
1) f1()
    What  does   the  above  statement  do  if  f1  is  a  regular  function ?  ---> Executes  f1()  function

2) f1()
    What  does  the  above  statement  do  if  f1  is  a  generator  function ?  ---> Creates  an  empty  generator  object

3) When  is  f1()  function  executed  in  case  of  generator ?  --->
																			As  soon  as  next(g)  is  executed  where  'g'  is   a  generator
'''
