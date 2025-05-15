#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
c = zip(a , b)  #   Creates  an  empty  zip  object
while   True:
	try:
		print(next(c))  #  ('Empno' , 25)  <next  line>  ('Emp Name' , 'Rama  Rao')  <next  line>  ('Salary ,10000.0)  <next  line
		time . sleep(1)
	except:
		break

'''

'''

'''
1) How  many  times  is  while  loop  executed ?  --->  4  times

2) What  happens  when  smallest  object  gets  exhausted ?  --->
													Remaining  elements  of  largest  object  are  ignored  and  throws  StopIteration  error
'''