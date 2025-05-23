#  Modify  following  program  with  'with'  statement
def   create(f):
	try:
		print('Type  text  terminated  by  ctrl+z')
		while  line :=  input():  #  Reads  each  line  from  keyboard  until  user  strikes  ctrl+z
				f . write(line + '\n')  #  Writes  each  line  to  the  file  along  with  '\n'
	except  EOFError:   #  Executed  when  user  strikes  ctrl+z
		print(F'File  {f . name}  is  created')
#  End  of  the  function
fname = input('Enter  filename :  ')  #  Read  filename
with  open(fname , 'w')   as  f:  #  Opens  the  file    in  'w' mode
		create(f)  #  Writes  user  input to  the  file
		print('Is  file  closed :  ' , f . closed) #  False :  In  with  statement
#  End of  with  statement
print('Is  file  closed :  ' , f . closed)  #  True :  Outside  with  statement