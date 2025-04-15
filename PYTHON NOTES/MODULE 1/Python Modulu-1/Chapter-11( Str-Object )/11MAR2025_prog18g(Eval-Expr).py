'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result

Hint:  Use  split()  method
'''
try:
	a = input('Enter the expression: ')  #  10*20
	sum = 0
	for x in a . split('+'):  # ['10*20']
		sum +=  eval(x)  #  sum = 0 + 23 + 456 + 7
	print('Sum: ', sum)
except:
	print('Invalid expression')
