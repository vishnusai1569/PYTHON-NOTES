'''
Write  a  program  to  print  employee  data  passed  from  command  line

Eg:  py  prog6.py   25   "Rama  Rao"   10000.0    m     False
                  0           1              2                3        4        5
'''
from  sys  import  argv
class   emp:  #  class  definition
	def  init(self):   #  self  is  object  'e'
		self . empno = int(argv[1])  #  How  to  copy  1st   input  from  argv  list  to  object   'e'
		self . ename = argv[2]  #  How  to  copy  2nd   input  from  argv  list  to  object   'e'
		self . sal = float(argv[3])  #  How  to  copy  3rd   input  from  argv  list  to  object   'e'
		self . gender = argv[4]  #  How  to  copy  4th   input  from  argv  list  to  object   'e'
		self . married = eval(argv[5])  #  How  to  copy  5th   input  from  argv  list  to  object   'e'
	def  disp(x):    # x    is  object  'e'
		print('Emp  number  :  ' ,  x . empno)  #  How  to  print  empno  which  is  in  object  'e'
		print('Emp  name    :  ' ,  x . ename)  #  How  to  print  ename  which  is  in  object  'e'
		print('Salary  :  ' ,  x . sal)  #  How  to  print  sal  which  is  in  object  'e'
		print('Gender  :  ' ,  x . gender)  #  How  to  print  gender  which  is  in  object  'e'
		print('Married  :  ' ,  x . married)  #  How  to  print  married  which  is  in  object  'e'
#End  of  the  class
try:
	e = emp()  #  How  to  create  emp  class  object
	e . init()  #  How  to  initialize  object  'e'
	e . disp()  #  How  to  print  object  'e'
except  IndexError:
	print('Send  inputs  in  the  order  empno  , emp  name , salary , gender  and  marital  status')
except  ValueError:
	print('Emp  name  should  be  in  double  quotes  (or)  Send  inputs  in  the  order  empno  , emp  name , salary , gender  and  marital  status')


#  object  'e'   --->  empno = 25 , ename = 'Rama Rao' ,  sal =  10000.0 , gender = 'm' , married = True



'''
1) py   prog6.py   25   "Rama    Rao"   10000.0   m   True
    What  does  the  above  command  do ? ---> Prints  all  the  command  line  inputs

2) py  prog6.py
    What  is  the  issue  with   the  above  command ? ---> argv[1]  throws  IndexError  becoz   index  1  does  not  exist

3) py   prog6.py   25   Rama   Rao   1000.65   m   True
    What  is  the  issue  with   the  above  command ? --->
																			float('Rao')  throws  error  becoz  "Rao"  can  not  be  converted  to  float

4) py   prog6.py   25   'Rama  Rao'   1000.65   m   True
    What  is  the  issue  with   the  above  command ? --->
																		float("Rao'")   throws  error  becoz  "Rao'"  can  not  be  converted  to  float

'''
#5) py   prog6.py   25   '''Rama  Rao'''   1000.65   m   True
#    What  is  the  issue  with   the  above  command ? --->
#												float("Rao'''")   throws  error  becoz  "Rao'''"  can  not  be  converted  to  float

'''
6) py   prog6.py   Rajesh   25   m   True   1000 . 65
    What  is  the  issue  with   the  above  command ? --->
															int('Rajesh')  throws  error  becoz   'Rajesh'   can  not  be  converted  to  int

7) Therefore  send  inputs  in  the  order  empno , ename , salary , gender  and  marital-status

8) What  does  classname()  do ? --->  Creates  an  object

9) Command  line  inputs  -------->  argv  list  ----------->  object  'e'  --------->  monitor
                                            PVM                          init()                           disp()

'''
