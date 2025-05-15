'''
Write  a  program  to  determine  largest  command  line  input

1) py   prog2.py   10     20     30.8    7   40    35.6
    What  is  the  largest  command  line  input ?  --->	40
    What  is  argv ?  ---> ['prog2.py' , '10' , '20' , '30.8' , '7' , '40' , '35.6']
    What  is  list  'a' ?  --->  [10 , 20 , 30.8 , 7 , 40 , 35.6]
    How  to  determine  largest  element  of  list  'a' ?  ---> max(a)  i.e.  40
    What  is  the  result  of  max(argv[1:]) ?  --->  '7'
    What  is  the  issue  with  max(argv[1:])) ?  --->  Largest  string  is  obtained  but  not  largest  number

2) py  prog2.py
    What  is  the  output ?  --->	Pls  send  inputs

3) py   prog2.py   'Rama'   'Sita'   'Rajesh'   'Manohar'   'Vamsi'   'Amar'
    What  is  the  largest  command  line  input ?  --->	'Vamsi'

4) py   prog2.py   25   'Ten'
    What  is  the  output ?  ---> Inputs  can  not  be  number  and  string

5) Hint1: Use  for  loop

6) Hint2: Use  try  and  except
'''
from sys import argv
try:
	a = []
	for  x  in  argv[1:]:
		a . append(eval(x))   #  ['Rama' , 'Sita'
	print('Largest  input :  ' , max(a))
except  ValueError:
	print('Send  at  least  one  number')
except  NameError:
	print('Input  strings  have  to  be  in   single   (or)   triple  quotes')
except TypeError:
	print('Send  number  inputs  (or)  string  inputs  but  not  both')


'''
1) py  prog2.py
    What  is  argv[1:] ?  --->  []
    What  is  the  issue  with  the  above  command ?  --->  max([ ])  throws  ValueError

2) py   prog2.py   'Hyd'  'Sec'  'Cyb'
    What  is  argv[1:] ?  ---> ["  'Hyd'  ", "  'Sec'  " , "  'Cyb'  "]

3) Same  thing  for  triple  quotes  also

4) py   prog2.py   Hyd  Sec  Cyb
    What  is  argv[1:] ?  --->  ['Hyd' , 'Sec' , 'Cyb']
    What  is  the  issue  with  the  above  command ?  --->  eval('Hyd')  returns   object  Hyd  which  does  not  exist

5) py   prog2.py   "Hyd"   "Sec"   "Cyb"
    What  is  argv[1:] ?  --->  ["Hyd" , "Sec" , "Cyb"]
    What  is  the  issue  with  the  above  command ?  --->  eval("Hyd")  returns   object  Hyd  which  does  not  exist

6) py   prog2.py   25   'Ten'
    What  is  argv[1:] ?  --->  ['25' , "  'Ten'  "]
    What  is  the  issue  with  the  above  command  ?  --->
											max([25 , 'Ten'])  throws  TypeError  becoz  number  and  string  can  not  be  compared

7) What  happens  when  error  is  raised ?  --->  Rest  of  the  program  is  skipped  and  except  suite  is  executed

8) What  is  the  advantage  of  handling  error ? --->  Error  is  not  reproted
																									and
																					 user  friendly  message  is  printed
'''
