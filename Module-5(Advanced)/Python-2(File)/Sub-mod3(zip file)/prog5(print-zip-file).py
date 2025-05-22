'''
Write  a  program  to  print  each  file  of  zipfile

Let  zip  file  contain  1.py , 2.txt , 3.py , 4.txt

1) Print  each  file  name  and   file  contents

2) Also  execute  the  file  if  it  is  a  py  file

3) How  to  execute  python  file  from  python  program ?  --->   os . system('py   filename.py')
'''
from  zipfile  import  ZipFile
import  os
def  disp(fname):
	f = open(fname , 'r')  # opens  the  file  in  read  mode
	str = f . read()  #   Reads  whole  file  into  a  str  object
	print('Contents  of the file :  ' , fname)
	print(str) #  prints  the  file  contents
	if  fname . endswith('.py'):
		print(F'Execution  results  of  {fname}')
		os . system(F'py  {fname}')  #  Execute  the  file  if  it  is  a  py  file
	f . close()  #  closes  the  file
def  display(z):
	list = z . namelist()#   All  the  files  of  zip  file  are  stored in  a  list
	os . system('cls')#  Clears  screen
	for  fname  in  list:  # fname  is  each  file  of  the  list
		disp(fname)  #  prints   each  file  of   zip  file
		os . system('pause')  # pauses  execution  after  printing  each   file
		os . system('cls') #  Clears   existing  file   before  printing  next  file
# End  of  the  function
try:
	filename = input('Enter  zip  filename  :  ')#   Reads  zip  filename
	z = ZipFile(filename , 'r')  #  zip  File  is  opened  in  read  mode  by   constructor  of  ZipFile
	display(z)  #  Prints each  file  of  zip  file
	z . close() #  Closes  zip  file
except  FileNotFoundError:
	print(F'File  {filename}  does  not  exist')