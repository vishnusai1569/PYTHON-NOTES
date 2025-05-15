'''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' =  'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->  Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  ---> Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop
'''
a = input('Enter  any  string  :  ')  #  RAMA RAO
even = odd = ''
for  i  in   range(len(a)):
	if   i % 2   ==  0:
		even  += a[i]  #  even = '' + 'R' + 'M' + ' ' + 'A'
	else:
		odd  += a[i]  #  odd = '' + 'A' + 'A' + 'R' + 'O'
#end  of  the  for  loop
print('Characters  at  even  indexes  :' , even)
print('Characters  at  odd  indexes  :' , odd)



'''
 0     1     2       3     4    5      6    7
 R     a     m      a            R     a     o

    i      i % 2 == 0        even	  object         odd  object
-----------------------------------------------------------------------------
                                        ''                           ''
   0           True                 'R'                        ''
   1            False                'R'                        'a'
   2            True                'Rm'                     'a'
   3            False                'Rm'                     'aa'
   4            True                 'Rm '                    'aa'
   5            False                'Rm '                    'aaR'
   6            True                'Rm a'                   'aaR'
   7            False                'Rm a'                   'aaRo'

What  is  the  difference  between  a[i]  and  'i' ?  --->  a[i]  is  each  character  of  the  string  and
																					    'i'  is  index  of  each  character
'''
