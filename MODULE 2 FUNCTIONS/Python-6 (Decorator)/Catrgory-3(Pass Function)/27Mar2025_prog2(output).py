#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun):  # fun  is  None
	print('f2  function')
	#fun() #   None()  throws  error  as  None  is  not  a  function
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1())  #  f2(None)
print('End')


'''
Begin
f1  function
f2  function
Back  to  f2  function
End
'''
