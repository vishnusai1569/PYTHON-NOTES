'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? ---> Found

3) Do  not  generate  fibonacci  series
'''
x = int(input('Enter  value  to  be  searched :  '))
if  x == 0:
	print('Found')
else:
	a = 0
	b = 1
	c = a + b
	while  c <= x:
		if  c == x:
			print('Found')
			exit()
		a = b
		b = c
		c = a + b
	print('Not  Found')
