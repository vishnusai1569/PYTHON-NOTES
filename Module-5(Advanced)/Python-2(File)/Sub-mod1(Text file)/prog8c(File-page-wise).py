'''
Write  a  program  to  print  file  pagewise  and  page  length = 20   lines

Let  file  contain
Rama  Rao
9247
+-$
Hyd is green city

 File -------> str  obj   ----------> list --------->  monitor
         read()                    split()          for  loop
'''
import  os
def  disp(f):  #   How  to  print  each  line  of  the  file  and  pause  execution  for  every  20  lines
	print(F'Contents  of   the   file  {f . name}')
	s = f . read()
	list = s . split('\n')
	ctr = 0
	for   x  in   list:
		print(x)
		ctr += 1
		if  ctr % 20 == 0:
			os . system('pause')
			os . system('cls')
# End  of  the  function
try:
	fname = input('Enter  filename  :  ')  #  How  to  read  filename
	f = open(fname , 'r')  #  How  to  open  the  file
	disp(f)  #  How  to  call  disp()  function
	f . close()  #   How  to  close  the  file
except:
	print(F'File  {f . name}   does  not  exist')



'''
1) Let  file  contain
    Rama  Rao
    9247
    +-$
    Hyd is green city
     s = f . read()
    What  does  str  object  's'  contain ?  ---> 'Rama Rao\n9247\n+-$\nHyd is green city\n'

2) list = s . split('\n')
    What  does  list  contain ?  --->  ['Rama Rao' , '9247' , '+-$' , 'Hyd is green city']
'''