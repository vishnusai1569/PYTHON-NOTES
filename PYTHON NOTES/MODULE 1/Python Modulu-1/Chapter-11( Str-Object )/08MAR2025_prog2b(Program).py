'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
'''
a = input('Enter first string: ')  #   H
b = input('Enter second string: ') #  PYTHON
if len(a) < 2 or len(b) < 2:
	print('Input  should  be  a  min  of  2-char  string')
else:
	print('Result  :  ' ,  b[: 2] + a[2 :] + ' ' + a[: 2] + b[2 :])  #   'PY' + 'VA' + ' ' + 'JA' + 'THON'



'''
1) What  is  the  result  of  str[:2]  ?  --->  First  two  characters  of  the  string

2) What  is  the  result  of  str[2:]  ?  --->  Whole  string  without  first  two  characters
'''
