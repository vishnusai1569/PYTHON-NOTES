'''
Repeat  prog8c(File-page-wise)   with  readline()  method

1) Let  file  contain
    Rama  Rao
    9247
    +-$
    Hyd is green city

2) File  a.txt   ----------> str  obj  ------------> monitor
                        readline()                    print()

3) Hint:  Use   while  loop  and  :=  walrus  operator
'''
import  os
def  disp(f):
	print(F'Contents  of   the   file  {f . name}')
	ctr = 0
	while  s := f . readline():   #  Reads  each  line  of  the  file  until  eof  is  reached
		print(s , end = '')  #  Prints  each  line  of  the  file
		ctr += 1  # Counts  number  of  lines  printed
		if  ctr % 20 == 0:  #  Suspends  execution  for  every  20  lines
			os . system('pause')  #  Next  20  lines  are  printed  after  user  strikes  a  key
			os . system('cls')  #  Clears   the  20  lines  before  printing  next  20  lines
#  End  of  the  function
try:
	fname = input('Enter  filename :  ')   #  Reads  the  filename
	f = open(fname)   #  Opens  the  file
	disp(f)  #  prints  file  pagewise
	f . close() #   Closes  the  file
except:
	print(f'File  {fname}  does  not  exist')


'''
1) How  many  times   is  while  loop  executed  if  the  file  has  63  lines?  --->  63  times

2) How  many  times  is  if  cond  true  ? --->  3  times
																		i.e.   End  of  20th  line , 40th  line  and  60th  line

3) How  many  pages  of  outputs  is  generated ?  --->  4  pages

4) How  many  lines  are  printed  in  each  of  the  first  three  pages ?  --->  20  lines
    How  many  lines  are  printed  in  4th  page?  ---> 3  lines
'''