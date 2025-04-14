# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):#  fun  is  div
	#How  to  decorate  the  function  such  that  4.5  is  returned
	def  inner(x , y):
		if  x > y:
			return  fun(x , y)  #  return  div(9 , 2)  --->  return  4.5
		else:
			return  fun(y , x)  #  return  div(9 , 2)  --->  return  4.5
	return  inner
@decor  #  Interpreted  as  div = decor(div)  --->  div = inner  i.e.  div  points to  inner()  function
def  div(a , b):
    return   a /b   #  Returned  to  function  call
print(div(9 , 2)) #  print(inner(9, 2))  --->  print(4.5)
print(div(2 , 9))  #  print(inner(2 , 9))  --->  print(4.5)
