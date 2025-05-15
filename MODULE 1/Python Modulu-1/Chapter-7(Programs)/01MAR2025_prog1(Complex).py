'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

Let  first  input   be  3 + 4j  and  second  input  be   5 + 6j
What  is  the  sum ? --->  (3 + 4j) + (5 + 6j) =  8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  --->  (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j)  =  (3 + 4j) * (5 - 6j) / (5 + 6j)  * (5 - 6j)
												=  (15 - 18j + 20j + 24) / (25 + 36)
												=   39 / 61  + 2j / 61
'''
try:
	x = complex(input('Enter first complex number : '))
	y = complex(input('Enter second complex number: '))
	print('Sum : ' , x + y)
	print('Difference : ' , x - y)
	print('Product: ' , x * y)
	print('Division : ' , x / y)
except:
	print('Input  should  be  complex  number')




'''
1) a = complex(input('Enter  1st   complex  number :  '))
    b = complex(input('Enter  2nd  complex  number :  '))
    What  are  values  of  a  and  b  if  inputs  are  3  and  4 ?  ---> 3 + 0j , 4 + 0j
    What  is  the  result  of  a + b ?  --->  	7 + 0j
    What  is  the  result  of  a - b ?  ---> -1 + 0j
    What  is  the  result  of  a * b ?  --->  12 + 0j
    What  is  the  result  of  a / b ?  ---> 0.75 + 0j

2) a = complex(input('Enter  1st   complex  number :  '))
    b = complex(input('Enter  2nd  complex  number :  '))
    What  are  values  of  a  and  b  if  inputs  are  3j  and  4j ?  ---> 3j   and  4j
    What  is  the  result  of  a + b ?  --->  7j
    What  is  the  result  of  a - b ?  ---> -1j
    What  is  the  result  of  a * b ?  --->  	-12 + 0j
    What  is  the  result  of  a / b ?  --->  0.75 + 0j

3) a = eval(input('Enter  1st   complex  number :  '))
    b = eval(input('Enter  2nd  complex  number :  '))
    What  are  values  of  a  and  b  if  inputs  are  3  and  4 ?   --->  3  and  4
    What  is  the  result  of  a + b ?  --->  7
    What  is  the  result  of  a - b ?  ---> -1
    What  is  the  result  of  a * b ?  --->  12
    What  is  the  result  of  a / b ?  ---> 	3 / 4 = 0.75
'''
