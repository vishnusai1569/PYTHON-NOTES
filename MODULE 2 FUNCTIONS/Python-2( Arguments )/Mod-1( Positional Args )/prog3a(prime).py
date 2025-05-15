'''
Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  --->  A  number  without  divisors  except  1  and  itself

2) Let  input  be  25
    What  is  the  range  of  divisors ? --->  i =   2 , 3 , 4 , 5 , 6 , ..... 12

3) Let  input   be  11
    What  is   the  range  of  divisors ? --->  i =  2 , 3 , 4 , 5

4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object

5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  ---> return   False

6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop
'''
def   prime(n):
	for  i   in   range(2 , n // 2 + 1):  # return  true   when  'n'  is  prime  number  and  False  otherwise
			if  n % i == 0:
				return  False
	# End of the  for  loop
	return  True
'''
1) prime(25)  --->  False
    How  many  times  is  for  loop  executed ?  --->  4  times

2) prime(11) --->  True
    How  many  times  is  for  loop  executed ?  ---> 4  times

3) prime(2) --->  True
    How  many  times  is  for  loop  executed ?  --->  0  times  due  to  empty  range  object

4) prime(49) ---> False
    How  many  times  is  for  loop  executed ?  --->  6  times

5) range(2 , n / 2 + 1)
    What  is  the  issue  with the  above  statement ?  --->  	/  is  a  float  operator  but  range()  can  not  have  float  operands

6) for  i  in  range(2 , n // 2 + 1):
	    if  n % i == 0:
				return   False
	   else:
   	            return  True
    What  are  the  two  issues  with  the  above  else ?  --->  for  loop  is  executed  only  once  and
								                                                               prime(25)  returns  True  even  though  25  is  not  a  prime  number

7) for  i  in  range(1 , n // 2 + 1):
	    if  n % i == 0:
				return   False
    What  is  the  issue  with  the  above  for  loop ? ---> Every  number  is  divisible  with  1  and  hence  start  from  2

8) for  i  in  range(2 , n):
	    if  n % i == 0:
				return   False
    What  is  the  issue  with  the  above  for  loop ? --->
																	There  are  no  divisors  beyond  n //  2  and  hence  don't  proceed  upto  n - 1

'''
n = int(input('Enter  any  number  :   '))  #  How  to  read  a  number
if  n < 2:   #   input  is  invalid:
	print('Invalid  input')
elif  prime(n):  #   input  is  prime  number:
	print('Prime  number')
else:
	print('Composite  number')
