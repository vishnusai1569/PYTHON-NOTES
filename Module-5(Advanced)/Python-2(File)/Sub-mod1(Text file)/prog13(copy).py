'''
Write  a  program  to  copy  contents  of  a  file  to  a  different  file

1) 1st    file   ---------->    str   object     -------->   2nd   file
                        read()                                write()

2) What  is  the  mode  in  which  is  1st  file  opened ?  ---> 'r'  mode
    What  is  the  mode  in  which  is  2nd  file  opened ?  --->  'w'   mode

3) What  action  to  be  made  when  1st  file  does  not  exist ?  --->  Print  a  message

4) What  action  to  be  made  when  2nd  file  does  not  exist ?  --->  Copy  1st  file  to  2nd  file

5) What  action  to  be  made  when  both  the  files  are  existing ? --->
										Copy  file  when  user  input  is  yes  and  print  a  message  when  user  input  is  no
'''
import os
def  copy(f1 , f2):
	s = f1 . read()  #   Reads  whole  text  of   1st  file  to  str  object  's'
	f2 . write(s)  #  Writes  str  object  to  2nd  file
try:
	fname1 = input('Enter first filename : ')  #  Reads  1st  filename
	f1 = open(fname1 , 'r')  #  Opens  1st  file  in  read  mode
	fname2 = input('Enter second filename : ')  #  Reads  2nd  filename
	if  os . path . isfile(fname2):  #  	Is  2nd  file  existing:
		ch = input(F'{fname2}  already  exists , overwrite (y/n) ? :  ')
		if  ch == 'y'  or  ch == 'Y':
			f2 = open(fname2 , 'w')  #  Opens  2nd  file  in  write  mode
			copy(f1 , f2) #  Copies  data  of  1st  file  to  2nd  file
			print(F'Contents  of  file  {fname1}  is  copied  to  {fname2}')
			f2 . close() #  Closes  2nd  file
		else:
			print('Program  terminates  without  copy')
	else:
		f2 = open(fname2 , 'w')  #  Opens  2nd  file  in  write  mode
		copy(f1 , f2) #  Copies  data  of  1st  file  to  2nd  file
		print(F'Contents  of  file  {fname1}  is  copied  to  {fname2}')
		f2 . close() #  Closes  2nd  file
	f1 . close() #  Closes  1st  file
except:
	print(F'File  {fname1}  does  not  exist')