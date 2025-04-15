'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
try:
	a = eval(input('Enter 1st input : '))
	b = eval(input('Enter 2nd input : '))
	c = eval(input('Enter 3rd input : '))
	if  a > b   and  a > c:
		print('Laregst  number  :  '  , a)
	elif  b > c:
		print('Laregst  number  :  '  , b)
	else:
		print('Laregst  number  :  '  , c)
except  NameError:
	print('Input  string  should  be  in  quotes')
except  TypeError:
	print('Input  can  not  be  a  complex  number')
