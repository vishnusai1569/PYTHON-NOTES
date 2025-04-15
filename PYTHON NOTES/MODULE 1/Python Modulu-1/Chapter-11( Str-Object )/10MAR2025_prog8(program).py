'''
Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0     1     2     3    4    5    6     7
 A    4     M    3    Z    5    D     2


Iteration        i       a[i]      a[i + 1]         out
--------------------------------------------------------------------------------
                                                              ''
     1               0       'A'         '4'             '' + 'A' + 'E' = 'AE'

	 2              2       'M'         '3'             'AE' + 'M' + 'P' = 'AEMP'

	 3              4       'Z'         '5'             'AEMP' + 'Z' + '_' = 'AEMPZ_'

	 4              6       'D'         '2'             'AEMPZ_' + 'D' +'F' = 'AEMPZ_DF'
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord()  functions
'''
try:
	a  =  input('Enter  any  string  with  alternate  character  and  digit  :  ')
	b = ''
	for  i   in   range(0 , len(a) , 2):
		b +=  a[i] + chr(ord(a[i]) + int(a[i + 1]))
	print('Result  :  ' , b)
except:
	print('Pls  enter  string  with  alternate  char  and  digit')
