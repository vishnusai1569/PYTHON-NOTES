'''
Write  a  function  to  return  average  of  numbers  in  the  file

Let  file  contain
10
20.8
True
15
18.4
eof

sum = 0 + 10 + 20.8 + True + 15 + 18.4
ctr = 0 + 1 + 1 + 1 + 1 + 1
'''
def   avg(f):
	sum = ctr = 0
	for  line  in   f:
		sum +=  eval(line)
		ctr += 1
	# End  of  for  loop
	return  sum / ctr
#  End  of  the  function
try:
	fname = input('Enter filename : ')   #  num.txt
	f = open(fname, 'r') #
	print(F'Average :  {avg(f):.2f}')
	f . close()
except  FileNotFoundError:
	print('File  does  not  exist')
except  NameError:
	print('File  can  not  have  string')
except  SyntaxError:
	print('File  can  not  have  blank  line')




'''
1) Can  file  have  integers , floats   and  booleans ?   --->  Yes  due  to  eval()  function

2) Can  file  have  strings ?  --->   No  and  eval('one')  throws   error

3) Can  file  have  blank  lines ?  --->  No

4) What  happens  when  there  is  a  blank  line   in  the  file ?  --->
														'\n'  is  read  from  the  file  and  eval('\n')  throws   SyntaxError

5) What  is  the  pre-requisite  to  run  the  program ?  --->
																	Type  numbers  in  the  file   and  save   the  file
																	i.e. Be  ready  with  the  file
'''