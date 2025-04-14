#  return  statement  demo  program
def  f1():
	print('f1  function')
	return  25  #  25  is  returned  to  function  call  f1()
	print('Hello')  #  Skipped  due  to   return
# End  of  the  function
print('Begin')
x =  f1()  #  x = 25
print(x)
print('End')


'''
Begin
f1  function
25
End
'''

'''
1) How  to  move  out  of  the  loop  ?  --->  With  break  statement

2) How  to  move  out  of  the  program  ?  --->  With  exit()  function

3) How  to  move  out  of  the  function  ?  --->  With  return  statement

4) How  to   move  out  of  the  loop  iteration ?  --->  With  continue  statement
'''
