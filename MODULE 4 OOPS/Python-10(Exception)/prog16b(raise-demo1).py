#  Find  outputs
def  f1():
	print('f1  function')
	raise   ValueError('Hyd')
	print('Sec') #   Skipped  due to  raise
# End of  the  function
#f1()  #  raises  ValueError  which  can not be  caught
try:
	print('Begin')
	f1()
	print('Bye') #   Skipped  :  Error is  not  yet  caught
except  ValueError  as  msg: #  msg  is   'Hyd'
	print('Caught  ValueError  outside  the  function  :  ' , msg)
#f1()  #  raises  ValueError  which  can not be  caught
print('End of the program')

'''
Begin
f1  function
Caught  ValueError  outside  the  function  :   Hyd
End of the program
'''


'''
1) Where  can  f1()  function  be  called  ?  --->
									Inside  try  suite  becoz  f1()  function  throws  an  error  and  not  caught  by  f1()  function

2) What  happens  when  f1()  is  called  outside  try  suite ?  --->  ValueError  is  reported
'''