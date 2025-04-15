'''
Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->   HVYADMSI

             0     1    2
a  --->   H     Y    D

              0    1     2     3    4
b  --->    V    A    M    S    I


i       a[i]        b[i]          c
--------------------------------------------------------
                                    ''
0     'H'        'V'           '' + 'H' + 'V' = 'HV'
1     'Y'         'A'           'HV' + 'Y' + 'A' =  'HVYA'
2     'D'         'M'          'HVYA' + 'D' + 'M' =  'HVYADM'
--------------------------------------------------------
1) What  action  to  be  made  when  1st  string  got  exhausted ?  --->  Concatenate  remaining  chars  of  2nd    string  to  object  'c'

2) What  action  to  be  made  when  2nd  string  got  exhausted ?  --->  Concatenate  remaining  chars  of  1st  string  to  object  'c'

3) Hint:  Use  while  loop  and  slice (outside)
'''
a = input('Enter  first  string  :  ')  #   HYD
b = input("Enter  second  string  :  ")  # VAMSI
c = ''
i = 0
while  i  <=  len(a) - 1   and   i <=  len(b) - 1:
	c  += a[i] + b[i]
	i += 1
if  len(a) > len(b):
	c += a[i :]
else:
	c += b[i:]
print('Result  :  ' , c)


'''
1) What  is   the  difference  between  a[i]   and  b[i] ? --->  a[i]  is  each  character  of  1st  string  and
																							   b[i]  is  each  character  of  2nd  string

2) length = max(len(a) , len(b))
    for  i  in  range(length):
	    if  i < len(a):
		    result += a[i]
	    if  i < len(b):
		    result += b[i]
'''
