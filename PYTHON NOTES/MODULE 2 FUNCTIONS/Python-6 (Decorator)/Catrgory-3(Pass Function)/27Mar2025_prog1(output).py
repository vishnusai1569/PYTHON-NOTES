#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2(fun): #   fun  poins  to  function  f1
	print('f2  function')
	fun()  #   f1()  i.e.  Executes  function   f1  thru  ref   fun
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1)  #  Passes  function  f1  to  function  f2
print('End')



'''
Begin
f2  function
f1  function
Back  to  f2  function
End
'''
