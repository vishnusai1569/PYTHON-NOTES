'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''
a = input('Enter  any  string : ')  #   HYD
b = ' '
if len(a) >=  4:
	b = a[:2] + a[-2:]  #  'PY' + 'ON'
print('Result : ' , b)



'''
1) What  is  the  result  of  str[-2 : ] ?  --->  Last  two  characters  of  the  string
    What  is  the  result  of  str[-3 : ] ?  --->  Last  three  characters  of  the  string
    What  is  the  result  of  str[-1 : ] ?  --->  Last  character  of  the  string

2) How  to  obtain  first  two  characeters  of  the  string ?  --->  str[:2]
    How  to  obtain  last  two  characeters  of  the  string ?  --->  str[-2:]
'''
