'''
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  --->  1/4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  --->  1
'''
def  power(a , b):
	if b > 0:
		return  a * power(a , b - 1)
	if  b < 0:
		return  1 / a  * power(a , b + 1)
	return  1
'''
1) power(4.5 , 3) = 4.5 * power(4.5 , 2)
                          = 4.5 * 4.5 * power(4.5 , 1)
                          = 4.5 * 4.5 * 4.5 * power(4.5 , 0)
                          = 4.5 * 4.5 * 4.5 * 1
						  = 4.5 ^ 3

2) power(4.5 , -3) = 1 / 4.5 * power(4.5 , -2)
                            = 1 / 4.5 * 1 / 4.5 * power(4.5 , -1)
                            = 1 / 4.5 * 1 / 4.5 * 1 / 4.5 * power(4.5 , 0)
                            = 1 / 4.5 * 1 / 4.5 * 1 / 4.5 * 1
							= 1 / 4.5 ^ 3

3) How  many  function  calls  are  in  power(a , b)  ? --->  |b| + 1
'''
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print(F'{a} ^ {b} = {power(a , b)}')   # How  to  print  a , b  and  a ^ b
