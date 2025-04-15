'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
try:
	year = int(input('Enter  4-digit  year :  '))
	if  year % 4 ==0  and  year % 100 != 0  or  year % 400 == 0:
		print('Leap year')
	else:
		print('Not a leap year')
except:
	print('Input  should  be  an  integer')
