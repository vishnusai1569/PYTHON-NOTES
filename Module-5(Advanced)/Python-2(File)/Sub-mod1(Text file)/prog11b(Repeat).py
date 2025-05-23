'''
Repeat  prog8c(File-page-wise)  with  readlines()  method


 File   ----------------->   list   --------------->    monitor
              readlines()                    for  loop

'''
import  os
def  disp(f):
	print(F'Contents  of   the   file  {f.name}')
	list = f . readlines()  #  Reads  all  the  lines  of   the  file  into a   list
	ctr = 0
	for  x  in   list:  #  'x'  is  each  line  (or)  element   of  the  list
		print(x , end = '')  #   Prints  each  line  (or)  element  of  the  list
		ctr += 1 #  counts  number  of  lines  printed
		if  ctr % 20 == 0:  #  Suspends  execution  for  every  20  lines
			os . system('pause')  #  Next  20  lines  are  printed  after  user  strikes  a  key
			os . system('cls')  #  Clears   the  20  lines  before  printing  next  20  lines
# End  of  the  function
try:
	fname = input('Enter  filename :  ')   #  Reads  the  filename
	f = open(fname)   #  Opens  the  file
	disp(f)  #  prints  file  pagewise
	f . close() #   Closes  the  file
except:
	print(f'File  {fname}  does  not  exist')