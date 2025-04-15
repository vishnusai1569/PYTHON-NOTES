'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  ---> 0 , 1 , 1 , 2 , 3 , 5 , 8

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  --->  2nd  term + 1st  term
    What  is  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''
x = int(input('Enter  value  of  x  :  '))  # 0
if  x == 0:
	print('Fibonacci  series')
	print(0)
else:
	a = 0  #  First  term
	b = 1 #  2nd  term
	print('Fibonacci  Series')
	print(a)  #  0
	print(b)  # 1
	c = a + b #  1
	while  c <= x:
		print(c)   #  1
		a = b  #   1
		b = c #  1
		c = a + b  #  2

