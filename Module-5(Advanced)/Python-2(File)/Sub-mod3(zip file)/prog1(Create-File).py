# Write  a  program  to  create  a  zip  file
from  zipfile  import  ZipFile
try:
	fname = input('Enter  filename  :  ')  #  Reads  file  name
	z = ZipFile (fname , 'w')  #  File is  opened  by  constructor  of  ZipFile  in  write  mode
	z . write('1.py')  # Writes  1.py  to  zip  file
	z . write('2.py')  # Writes  2.py  to  zip  file
	z . write('5.py')  #  Error :  5.py  file  does  not  exist
except   FileNotFoundError   as   msg:  #   Executed  :  5.py  file does  not exist
	z . write('3.txt') # Writes  3.txt  to  zip  file
	z . write('4.txt')  # Writes  4.txt  to  zip  file
	z . close()  #  closes  zip  file
	print(F'File  {fname} is  created  with  4  files')









'''
After  running  the  program,  open  a.zip  file  in  file  exlporer  and  observe
that  there  are  4  files  in  a . zip
'''