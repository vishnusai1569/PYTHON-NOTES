'''
Repeat  prog5b(File-Create)  with  writelines()  method

1) Let  input  be
    Rama  Rao
    9247
    +-$
    Hyd is green city
    ctr+z

2) Keyboard   ------------->   str  object  ----------------->  list  ------------------->   File
                          input()                                 append()                      writelines()
'''
def  create(f):
	try:
		print('Enter  text  terminated  by  ctrl + z')
		a = []    #  Empty  list
		while  line := input():  #  Reads  each  line  from  keyboard  until  user  strikes  ctrl+z
			a . append(line + '\n')  #  Appends  each  line  to  the  list  along  with  '\n'
	except  EOFError:  #  Executed  when  user  strikes  ctrl+z
		f . writelines(a)  #  Writes  strings  (or)  elements  present  in  the  list  to  the  file
		print(F'File  {f.name}  is  created')
#  End  of  the  function
fname =  input('Enter  filename :  ')  #  Reads  the  filename
f = open(fname , 'w')  # Opens  the  file  in  write  mode
create(f)  #  Writes  user  input  text  to  the  file
f . close()  #  Closes  the  file