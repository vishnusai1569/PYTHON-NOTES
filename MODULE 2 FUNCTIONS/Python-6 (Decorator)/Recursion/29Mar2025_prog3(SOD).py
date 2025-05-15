'''
Write  a  recursive  function  to  find  sum of  the  digits  of  a  number

sod(678) =  678 % 10 + sod(678 // 10)
               =  8 + sod(67)
               =  8 + 67 % 10 + sod(67 // 10)
               =  8 + 7 + sod(6)
               =  8 + 7 + 6 % 10 + sod(6 // 10)
               =  8 + 7 + 6 + sod(0)
               =  8 + 7 + 6 + 0
               =  21

1) How  many  function  calls  are  in  sod(678) ?  --->  4

2) How  many  function  calls  are  in  sod(n-digit  number) ?  --->  n + 1
'''
def   sod(n):
	if  n > 0:
		return  n % 10 + sod(n // 10)
	else:
		return   0
'''
1) sod(9427) = 7 + sod(942)
                    = 7 + 2 + sod(94)
                    = 7 + 2 + 4 + sod(9)
                    = 7 + 2 + 4 + 9 + sod(0)
                    = 7 + 2 + 4 + 9 + 0
					= 22

2) Can  if  condition  be  changed  to  n  ==  0 ?  --->  Yes  provided  the  two  return  statements  are  interchanged
'''
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' , sod(n))
