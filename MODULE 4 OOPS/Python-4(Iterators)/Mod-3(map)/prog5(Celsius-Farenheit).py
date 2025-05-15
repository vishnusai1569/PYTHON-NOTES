'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  ---> 1.8 * celsius  temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''
import time
c = eval(input('Enter  list  of  celsius  temperatures :  '))
m = map(lambda  x : 1.8 * x + 32 , c)
print('Farenheit   temperatures')
for  y  in  m:
		print(y)
		time . sleep(1)



'''
1) What  is   the  value   of  'x' ?  --->  Each  element  of  list  'c'

2) Where  is   1.8 * x + 32  returned  to  ?  --->  for  loop  variable  'y'

3) How  to  define  regular  function  instead  of  lambda  function ?  --->  def   convert(x):
																															return  1.8 * x + 32

4) How  to  create  map  object  with  regular  function  ?  --->  m = map(convert , c)
'''