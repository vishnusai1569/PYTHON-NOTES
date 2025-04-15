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
'''
def   prime(n):
	count = 0
	if n<2:
		return False
	elif n==2:
		return True
	else:
		for i in range(2,int(n**0.5)+1):
			count+=1
			print(count)
			if n%i == 0:
				return False
	return True
	#return  true   when  'n'  is  prime  number  and  False  otherwise

a = int(input('Enter a number : '))#How  to  read  a  number
if   a<0:#input  is  invalid:
	print('Invalid  input')
elif  prime(a):#input  is  prime  number:
	print('Prime  number')
else:
	print('Composite  number')

1) prime(25)  ---> Composite  number
    How  many  times  is  for  loop  executed ?  --->4

2) prime(11) --->Prime number
    How  many  times  is  for  loop  executed ?  --->2

3) prime(2) --->Prime number 
    How  many  times  is  for  loop  executed ?  --->0

4) prime(49) --->Composite number
    How  many  times  is  for  loop  executed ?  --->6
'''

def prime(n):
	for i in range(2,n//2+1):
		if n%i==0:
			return False
	return True

a = int(input('Enter a number : '))#How  to  read  a  number
if   a<0:#input  is  invalid:
	print('Invalid  input')
elif  prime(a):#input  is  prime  number:
	print('Prime  number')
else:
	print('Composite  number')


