# Write  a  program  to  print  csv  file
import  csv
def  disp(f):
	r = csv . reader(f)  #  Returns  an  iterator
	for  list   in   r:  #  list  is  each  row  of   the  file
		for  x  in  list: #  'x'   is   each  element  of  the  file
			print(F'{x:10}' , end = '\t')
		print()
# End  of  function
try:
	fname = input('Enter  file  name :   ')  #  Reads  filename
	f = open(fname , 'r')  #  Opens  file   in   read  mode
	disp(f)
	f . close()
except  FileNotFoundError:
	print(F'File  {fname}  does  not  exist')


'''
1) What  does  outer  loop  do ?  --->   Iterates  thru  each  row  of  the  file

2) What  does  inner  loop  do ? --->  Iterates  each  element  of  the   list
'''