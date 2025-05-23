'''
Repeat  prog8c(File-page-wise)  with  for  loop

Let  file  contain
Rama  Rao
9247
+-$
Hyd is green city

File  ----------> str  obj  ------------> monitor
          for  loop                    print()
'''
import  os
def  disp(f):
	print(F'Contents  of   the   file  {f . name}')
	ctr = 0
	for  line   in   f:  #   Iterates  each  line  of  the  file  until  eof  is  reached
		print(line , end = '')  #  Prints  each  line  of   the  file
		ctr += 1 #  counts  number  of  lines  printed
		if  ctr % 20 == 0:  #  Suspends  execution  for  every  20  lines
			os . system('pause')  #  Next  20  lines  are  printed  after  user  strikes  a  key
			os . system('cls')  #  Clears   the  20  lines  before  printing  next  20  lines
	# End  of  for  loop
	print('Is  file  closed :  ' , f . closed)  #  False
# End  of  the  function
try:
	fname = input('Enter  filename :  ')   #  Reads  the  filename
	f = open(fname)   #  Opens  the  file
	disp(f)  #  prints  file  pagewise
	f . close() #   Closes  the  file
except:
	print(f'File  {fname}  does  not  exist')