#  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun): #  fun  is  f1
	def   inner():
		x = fun()  #  x = f1()  --->  x = 10
		return   x + 2 #  12  is  returned  to  function  call  f1()
	return  inner #  Returned  to  function  call  decor(f1)
def  f1():
        return  10  #  10  is  returned  to  function  call   fun()  i.e.  f1()
#end  of  the  function
f1 = decor(f1)  #  f1 = inner  i.e.  f1  points  to  inner()  function
print(f1())  # print(inner())  i.e.  print(12)

'''
12


1) What  is  the  issue  when  @decor  tag  is  omitted  ?  --->
																			decor()  function  has  to  be  called  explicitly  by  f1 = decor(f1)

2) Which  is  a  better  approach  ?  --->  @decor  tag

3) What  is  the  advantage  with  @decor  tag ?  --->  decor()  function  is  automatically  executed
'''
