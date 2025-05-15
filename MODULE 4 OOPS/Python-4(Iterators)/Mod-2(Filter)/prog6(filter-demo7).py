# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda   x  :   x[1]  >=  12 , list) #  Creates  an  empty  filter  object
while   True:
	try:
		print(next(f))  #   ('B' , 20)  <next  line>  ('C' , 15)    <next  line>  ('E' , 18)  <next  line>
		time . sleep(1)
	except:
		break


'''
1) What  is  'x'  in  the  lambda  function ?  --->  Each  tuple  of  the  list

2) What  is  x[1]  in  the  lambda  function ?  --->  2nd  element  of   tuple  'x'

3) How  to  define  regular  function  instead  of  lambda  function ?  --->  def   f1(x):
																														 return   x[1] >= 12

4) How  to  create  filter  object  with  regular  function ?  --->  f = filter(f1 , list)
'''