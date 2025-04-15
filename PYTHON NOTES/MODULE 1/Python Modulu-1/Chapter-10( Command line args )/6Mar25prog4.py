'''
Write  a  program  to  determine  average  of  command  line  inputs

1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
    What  is  argv ?  --->  ['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
    What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
	How  to  determine  sum  of  list  elements ?  ---> sum(a)
    How  to  determine  number  of  list  elements ?  --->	len(a)

2) py   prog4.py
    What  is  the  output ?  --->  Pls  send  number  inputs

3) py   prog4.py  25    Ten
    What  is  the  output  ?  ---> Pls  send  number  inputs
'''
from sys import argv
try:
	a = []
	for  x  in  argv[1:]:
			a . append(eval(x))  #   [25 , 'Ten']
	else:
			print('Average  :   ' , sum(a) / len(a))
except ZeroDivisionError:
	print('Send  at  least  one  input')
except  (TypeError , NameError):
		print('Do  not  send  string')


'''
1) py  prog4.py
    What  is  the  issue  with  the  above  command ? ---> 0 / 0  throws  ZeroDivisionError
    What  is  argv[1:] ?  --->  []
    What  is  sum([]) ?  --->	0
    What  is  len([]) ?  --->  0

2) py   prog4.py   25   Ten
    What  is  the  issue  with  the  above  command ? ---> eval('Ten')  returns   object  Ten   which  does  not  exist

3) py   prog4.py   25   'Ten'
    What  is  the  issue  with  the  above  command ? --->
													sum([25 , 'Ten'])  throws  TypeError  becoz  number  and  string  can  not  be  added

4) import   sys
    Is  print(argv)  valid ? --->  No  becoz  argv  can  not  be  used  as  it  is  not  imported
    What  is  the  alternative  ?  --->	print(sys . argv)

5) from  sys  import  argv
     Is  print(sys . argv)  valid ?  --->  No  becoz  sys  can  not  be  used  as  it  is  not  imported
     What  is  the  alternative  ?  --->  print(argv)
'''
