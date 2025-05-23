'''
Write  a  program  to  merge  two  files  to  form  a  new  file

1) Let  1st  file  contain  10  lines  and   2nd  file  contain  7  lines
    What  does  3rd  file  contain ?  ---> 10 + 7 = 17  lines

2) What  action  to  be  made  when  both  the  files  are  existing ?  --->  Merge  them  to  form  a  new  file

3) What  action  to  be  made  when  2nd  file  is  not  existing ?  --->  Copy  1st  file  to  3rd  file

4) What  action  to  be  made  when  1st  file  is  not  existing ?  --->  Copy  2nd  file  to  3rd  file

5) What  action  to  be  made  when  both  the  files  are  not  existing ?  --->  Print  a  message
'''
import  os
def  copy(file1 , file2):
	s = file1 . read()  #  Reads  whole  text  of  file1  to  str  object  's'
	file2 . write(s)  #  Writes  str  object  to  file2
#  End  of  the  function
fname1 = input('Enter  first  file  name : ')  #   Reads  1st  filename
fname2 = input('Enter  second  file  name : ')  #   Reads  2nd  filename
fname3 = input('Enter third  file  name : ')  #   Reads  3rd  filename
if  os . path . isfile(fname1)  and  os . path . isfile(fname2): #  Both  the  files  are  existing
	f1 = open(fname1 , 'r')  #   Opens  1st  file  in  read  mode
	f2 = open(fname2 , 'r')   #   Opens  2nd  file  in  read  mode
	f3 = open(fname3 , 'w')   #   Opens  3rd  file  in   write  mode
	copy(f1 , f3)  #  Copies  1st  file   to  3rd  file
	copy(f2 , f3)  #  Copies  2nd   file   to  3rd  file
	f1 . close()  #  Closes  all  the  3  files
	f2 . close()
	f3 . close()
	print(F'{fname1} and {fname2}  are  copied to {fname3}')
elif  os . path . isfile(fname1): #  1st  file  is   existing  but  not  2nd  file
	f1 = open(fname1 , 'r')  #   Opens  1st  file  in  read  mode
	f3 = open(fname3 , 'w')  #   Opens  3rd  file  in   write  mode
	copy(f1 , f3)#  Copies  1st  file   to  3rd  file
	f1 . close()  #  Closes  1st  and  3rd files
	f3 . close()
	print(F'{fname1}  is  copied  to  {fname3}')
elif  os . path . isfile(fname2):   #  2nd  file  is   existing  but  not  1st  file
	f2 = open(fname2 , 'r')  #   Opens  2nd  file  in  read  mode
	f3 = open(fname3 , 'w')  #   Opens  3rd  file  in   write  mode
	copy(f2 , f3)  #  Copies  2nd   file   to  3rd  file
	f2 . close() #  Closes   2nd  and  3rd files
	f3 . close()
	print(F'{fname2}  is  copied  to  {fname3}')
else:
	print('Both  the  files  are  not  existing')
	os . system(F'del  {fname3}')  #  Deletes  3rd  file




'''
os . system(F'del  {fname3}')
What  does  the  statement  do  ?  --->  Executes  dos  command  del
'''