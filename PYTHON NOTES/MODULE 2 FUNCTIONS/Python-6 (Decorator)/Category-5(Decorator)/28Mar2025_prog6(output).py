# Gift
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . __name__)
	def   inner(*x):
		print(x)
		fun(*x)
		print('End  of  decoration')
	return  inner #  Returned  to  function call
@decor  # Interpreted  as   f1 = decor(f1)  --->  f1 = inner  i.e.  f1  points  to  inner()  function
def   f1(x): #  x  is   10
	print('f1  function  :  ' , x)
@decor  # Interpreted  as   f2 = decor(f2)  --->  f2 = inner   i.e.  f2  points  to  inner()  function
def   f2(x , y): #  x  is  25  and  y  is  10.8
	print('f2  function  :  ' , x , y )
@decor  # Interpreted  as   f3 = decor(f3)  --->  f3 = inner   i.e.  f3  points  to  inner()  function
def  f3(x , y , z):#  x  is  'Hyd' , 'y'  is  True  and  'z'  is  3+4j
	print('f3 function : ' , x , y , z)
@decor  # Interpreted  as   f4 = decor(f4)  --->  f4 = inner   i.e.  f4  points  to  inner()  function
def   f4():
	print('f4 function')
# end of function
f1(10)  #  inner(10) , x  is  (10,)  and  *x  unpacks  tuple  to  10
f2(25 , 10.8)   #  inner(25 , 10.8) , x  is  (25,10.8)  and  *x  unpacks  tuple to  25  <space>  10.8
f3('Hyd' ,  True  , 3 + 4j)   #  inner('Hyd' ,  True  , 3 + 4j) ,  x  is  ('Hyd' ,  True  , 3 + 4j) and  *x  unpacks  tuple to  Hyd  <space>  True  <space>    3+4j
f4()  #  inner() ,  x  is  () and  *x  unpacks  empty  tuple to Nothing


'''
f1
f2
f3
f4
(10,)
f1  function  :   10
End  of  decoration
(25, 10.8)
f2  function  :   25 10.8
End  of  decoration
('Hyd', True, (3+4j))
f3 function :  Hyd True (3+4j)
End  of  decoration
()
f4 function
End  of  decoration
'''
