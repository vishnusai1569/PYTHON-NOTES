# Decorate  f1  function  such  that  it  returns  12
def   decor(fun):  #  fun  is   function  f1
	print("hi")  #   f1
	def   inner():
		return   fun() +  2  #   return  f1() +  2   --->  return  10 + 2  = 12  is   returned  to  function  call
	return  inner  #  Returned  to   function  call  decor(f1)
@decor  #  f1 = decor(f1)  ---> f1 = inner  --->  Ref  f1  points  to  inner()  function
def   f1():
	return  10  #  Returned  to  function  call    fun()
# End of the function
print(f1())  # print(inner())  --->  print(12)

'''
f1
12
'''

'''
1) return  f1() + 2
    What  is  the  issue  with  the  above  statement  in  inner  function ?  --->
																	f1()  becomes  inner()  which  leads  to  recursion (i.e.  infinite  recursion)

2) What  is  the  only  way  to  reach  f1()  function  from  inner  function ?  --->  Thru  reference  fun

3) What  does  f1  function  return  when  it  is  not  decorated ?  --->  10

4) What  does  f1  function  return  when  it  is  decorated ?  --->  12
'''
