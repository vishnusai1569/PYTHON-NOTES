'''
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

a = 10
b = 20
c = 7
max = 20
min =  7
mid =  (10 + 20 + 7) - (20 + 7) = 37 - 27 = 10

1) What  is  the  initial  value  of  max  ?  --->  a

2) Whichever  input >  max,  copy  that  input  to  max

3) What  is  the  initial  value  of  min  ?  --->  'a'

4) Whichever  input  <  min,  copy  that  input  to  min

5) How  to  obtain  middle  number ?  --->   Eliminate  max  and  min  from  a , b , c
'''
a = float(input('Enter  first  input   :  '))
b = float(input('Enter  second   input   :  '))
c = float(input('Enter  third  input   :  '))
max = a
if b > max:
	max = b
if c > max:
	max = c
min = a
if  b < min:
	min = b
if  c < min:
	min = c
mid = (a + b + c) - (max + min)
print('Largest number : ' , max)
print('Smallest number : ' , min)
print('Middle number : ' , mid)
