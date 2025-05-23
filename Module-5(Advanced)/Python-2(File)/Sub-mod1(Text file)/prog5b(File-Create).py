'''
Write  a  program  to  create  a  text  file  with  user  input  text  terminated  by  ctrl+z

1) Let  input  be
    Rama  Rao
    9247
    +-$
    Hyd is green city
    ctr+z

2) Keyboard  ------->   str  object  ------------>    File
                     input()                          write()

3) What  is  ctrl + z ?  --->  End  of  inputs

4) What  does  input()  function  do  when  input  is  ctrl + z ?  --->  Reads  nothing  and  raise  EOFError
'''
def   create(f):
	try:
		print('Type  text  terminated  by  ctrl+z')
		while  line :=  input():  #  How  to  read  each  line  from  keyboard  and  write  to  the  file  until  user  strikes  ctrl+z
				f . write(line + '\n')
	except  EOFError:
		print(F'File  {f . name}  is  created')
#  End  of  the  function
fname = input('Enter  filename :  ')  #  How  to  read  the  filename  --->  a.txt
f = open(fname , 'w')  #   How  to  open  the  file
create(f)  #  How  to  call  create  function
f . close()  #  How  to  close  the  file


'''
1) f . write(line + '\n')
   What  is  the  issue  when  '\n'  is  omitted ?  --->  Writes  whole  text  to  the  file  in  same  line

2) f . write(line , '\n')
    Is  the  statement  valid ?  ---> No  due  to  two  arguments

3) f . write(line + '\n')
    What  does  +  do ?  --->  Concatenates  str  object  line  with  '\n'  and  writes  new  string  to  the  file

4) print(F'File  {f . name}  is  created')
     Can  f . name  be  replaced  with  fname ?   ---> Yes  becoz  fname  is  a  global  object
'''