'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
try:
	ch = int(input('Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  '))
	if ch == 1:
		c = float(input('Enter  celsius  temperature :  '))  # 30
		print('Fahrenheit  Equivalent  : ' , 1.8 * c + 32)
	elif  ch ==2:
		f= float(input('Enter  fahrenheit  temperature : '))
		print(F'celsius   equivalent :  {(f-32)/1.8:.2f}')
	else:
		print('Invalid input')
except:
	print('Input  should  be  a  number')
