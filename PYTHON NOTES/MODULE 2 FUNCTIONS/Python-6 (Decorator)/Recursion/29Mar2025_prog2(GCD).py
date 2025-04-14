'''
Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers

1) gcd(12 , 15) =  gcd(15 , 12) = gcd(12 , 3) = gcd(3 , 0) = 3

2) gcd(4 , 7) = gcd(7 , 4) = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''
def  gcd(m , n):
	if  n > 0:
		return  gcd(n , m % n)
	else: #  n  is  0
		return   m
'''
1) gcd(4 , 6)  --->  gcd(6 , 4)  --->  gcd(4 , 2)  --->  gcd(2 , 0)  --->  2

2) Can  if  condition  be  changed  to  n  ==  0 ?  --->  Yes  provided  the  two  return  statements  are  interchanged
'''
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,   gcd(m , n))
