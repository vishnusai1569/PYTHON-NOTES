'''
Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  --->  ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  ---> a . sort()
    How  to  sort  list  'a'  in  descending  order  ?  --->  a . sort(reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together
'''
from sys import argv
try:
	a=[]
	for x in argv[1:]:
			a.append(eval(x))  #   ['Hyd' , 'Sec' , 'Cyb]
	a . sort()
	print('Ascending  order :  ' , a)
	a . sort(reverse = True)
	print('Descending  order :  ' , a)
except  TypeError:
	print('Do  not   send  number  and  string')
except  NameError:
	print('String  has  to  be  in  single  (or)  triple   quotes')



'''
1) py  prog5.py   'Hyd'   'Sec'   'Cyb'
    Are  single  quotes  mandatory ?  --->  Yes  due  to  eval()  function
'''

#2) py  prog5.py  '''Hyd'''   '''Sec'''   '''Cyb'''
'''   Are  triple  quotes  mandatory ?  --->  Yes  due  to  eval()  function

3) py  prog5.py   "Hyd"   "Sec"   "Cyb"
    What  is   the  issue  with  the  above  command ?  --->  eval("Hyd")  returns  object  Hyd  which  does  not  exist

4) py  prog5.py   Hyd   Sec   Cyb
     What  is   the  issue  with  the  above  command ?  ---> eval('Hyd')  returns  object  Hyd  which  does  not  exist

5) py  prog5.py
    What  is  the  output  of  above  command ?  ---> []  twice

6) py  prog5.py  25   'Ten'
    What  is  the  issue  with  the  above  command ?  --->
																		a . sort()  throws  error  becoz  number  and  string  can  not  be  sorted
'''
