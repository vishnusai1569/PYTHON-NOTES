#  Write  a  program  to  print  month  calendar
import  calendar
try:
	mnth  =  int(input('Enter  month (1 - 12) :  '))  #  8
	year = int(input('Enter  year  :  ')) #  1947
	print(calendar . month(year , mnth))
except:
	print('Input  month  number  should  be  between  1  and  12')


'''
month()  function
--------------------
1) What  does  month()  function  do  ?  --->  Returns  month  calendar

2) What  are  the  two  arguments  of  month()  function ?  --->  Year  and  month

3) What  does  month(2021 , 4)  do ?  ---> Returns  April  2021  calendar

4) Is  month(2099 , 13)  valid  ?  --->  No  becoz  month  13  is  invalid  month  number

5) Where  is  month()  function  defined ?  ---> In  calendar  module
'''
