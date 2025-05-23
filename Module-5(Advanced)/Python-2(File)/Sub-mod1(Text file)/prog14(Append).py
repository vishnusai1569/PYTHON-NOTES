'''
Write  a  program  to  append  contents  of  a  file  to  another  file

1) What  is  the  mode  in  which  can  1st  file  be  opened ?  --->  'r'   mode
    What  is  the  mode  in  which  is  2nd  file  opened ?  ---> 	'a'  mode

2) Where  does  file  handle  points  to  when  file  is  opened  in  append  mode ?  --->  End  of  the  file
    Where  does  file  handle  points  to  when  file  is  opened  in  read  or  write  mode ? ---> Begining  of  the  file

3) What  action  to  be  made  when  1st  file  does  not  exist ?  --->  Print  a  message

4) What  action  to  be  made  when  2nd  file  does  not  exist ?  --->  Copy  1st  file  to  2nd  file

5) What  action  to  be  made  when  both  the  files  are  existing ? --->  Append  1st  file  contents  to  2nd  file
'''
try:
	fname1 = input('Enter first filename : ')  #  Reads  1st  file  name
	f1 = open(fname1 , 'r')  #  Opens  1st  file  in  read  mode
	fname2 = input('Enter second filename : ')   #  Reads  2nd  file  name
	f2 = open(fname2 , 'a')  # Opens  2nd  file  in  append  mode
	s = f1 . read()  #  Reads  whole  text  of  1st  file  to  str  object  's'
	f2 . write(s)  #  Writes  str  object  's'   at  the  end  of  2nd  file
	print(F'Contents  of  file  {fname1}  is  appended  or  copied  to  file  {fname2}')
	f1 . close()   #  Closes  1st file
	f2 . close()   #  Closes   2nd   file
except:
	print(F'File  {fname1} does  not  exist')