'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5

Hint:  Use  for  loop
'''
n = int(input('Enter number of terms : '))
print('Fibonacci series')
a = 0
print(a)
if  n > 1:
	b = 1
	print(b)
	c = a + b
	for  i  in   range(n - 2):
		print(c)
		a = b
		b = c
		c = a + b
