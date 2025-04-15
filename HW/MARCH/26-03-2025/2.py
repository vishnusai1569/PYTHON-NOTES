#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun):
	print('f2  function')
	fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1())
print('End')

def  f1():
	print('f1  function')
def   f2 (fun):
	print('f2  function')
	fun
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1())
print('End')

"""
begin
f1 function
f2 function
error

"""
"""
begin
f1 function
f2 function
back to f2 function
end

"""