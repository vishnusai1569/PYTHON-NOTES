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
	if  ???
		return  ???
	else:
		return  ???
'''
1) sod(9427) =
'''
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' ,  ???)