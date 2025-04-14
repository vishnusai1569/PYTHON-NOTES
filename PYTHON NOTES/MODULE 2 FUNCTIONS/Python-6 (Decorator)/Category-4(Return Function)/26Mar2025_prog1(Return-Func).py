# Find  outputs
def  outer():
	print('outer  function')
	def  inner():
		return  10  #   Returned  to   function  call  x()
	return  inner   #  Returned  to  function  call  outer()
# End  of  the  function
x = outer()  # x = inner  --->  'x'  points  to  inner()  function
print(x())  #  print(inner())  --->  print(10)
#print(inner())  #  Error  :  inner()  function  is  not  visible  outside  and hence  can  not be  called
print(outer()())  #  print(inner())  --->  10


'''
outer  function
10
outer  function
10


Function  returning  another  function
---------------------------------------------
1) How  to  return  a  function ?  --->  return  functionname

2) What  does  return  inner  do ?  --->  inner  function  is  retuned  to  the  outer  function  call  i.e.  outer()

3) What  is  the  advantage  of  returning  inner  function ?  --->
																It  can  be  called  indirectly  with  x()  from  outside  the  function

4) Can  inner  function  be  called  directly  from  other  functions  and  outside ?  --->  No  becoz  it  is  not  visible

5) return  inner
    return  inner()
    What  is  the  difference  between  the  above  two  statements ?  --->
																						return  inner   returns   inner  function  but
																						return  inner()  returns  result  of  inner()  function
'''
