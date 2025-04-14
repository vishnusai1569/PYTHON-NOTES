#  Find  outputs  (Home  work)
def   decor(fun):#  fun  is  f1
	print(fun . __name__)  #  Name  of  that  function  where  fun  points  i.e.  f1
	def   inner():
		return   fun() +  2
	return  inner #  Returned  to  function  call  decor(f1)
@decor  #  Interpreted  as  f1 = decor(f1)  --->  f1 = inner  --->  f1  points  to  inner()  function
def   f1():
	return  10
# End of the function
print('End')


'''
f1
End
'''
