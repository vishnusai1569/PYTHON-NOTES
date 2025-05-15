# Find  outputs  (Home  work)
def  square(fun):#   fun is  num
	def  inner1():
		x = fun()  #  x = num()  ---> x =  10
		return  x * x #   100  is  returned to  function call  inner1()
	return  inner1 #  Returned  to  function  call   square(num)
def   double(fun): #  fun  is  inner1
	def  inner2():
		y = fun() #   y = inner1()  --->  y = 100
		return  2 * y  #   200  is  returned to  function call  inner2()
	return   inner2   #  Returned  to  function  call   double(inner1)
@double  #  Interpreted  as  num = double(square(num))  --->  num = double(inner1)  --->  num = inner2  i.e.  num  points  to  inner2  function
@square
def  num():
	return  10 #  Returned  to function  call   fun() i.e  num()
#end of the function
print(num())  # print(inner2())  --->  print(200)


'''
@double
@square
@double
@square
def  num():
	return  10
What  is  the  result  if  num() ?  --->   10 **  2  ---> 100 * 2  --->  200 ** 2 --->  40000 * 2 --->  80000
'''
