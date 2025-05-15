# Find  outputs
import  time
class   c2:
	def  __init__(self):
		self . x = 0
	def  __iter__(self):  #  self  is   object  itr
		print('__iter__  method ')
		return   self
	def  __next__(self):  #  self  is   object itr
		self . x += 1  #
		if  self . x <= 3:
			print('__next__  method ')
			return   self . x
		raise  StopIteration
# End  of  the  class
itr  =  c2()  #  Object  is  initialized  with  x = 0
print('for  loop')
for  y  in   itr:  #   for   y   in   itr:
	print(y) #   3
	time . sleep(1)
print('while  loop')
itr  = c2()
while  True:
	try:
		print(itr . __next__())  #  3
		time . sleep(1)
	except:
		break



'''
1) for  y  in   c2():
	      pass
    Can  for  loop  use  c2  class  object  ?  --->  Yes  due  to  __iter__()  method  in  class  c2

2) Which  methods  are  executed  in  1st  iteration  of  for  loop ?  --->
																	__iter__()  and  __next__()  methods  are  automatically  executed

3) Which  method  is  executed  in  subsequent  iterations  of  for  loop ?  --->
																					Only  __next__()  method  is  automcatically executed

4) Can  __next__()  method  raise  ValueError  ? --->
												No  becoz  for  loop  internally  handles  only  StopIteration  error  but  not  any  other  error

5) Can  __iter__()  method  return  25 ?  --->  No  becoz  25  is  not  an  iterator

6) In  other  words,  __iter__()  method  can  return  iterator  only

7) What  happens  when   return   statement  is  omitted  from   __iter__()  method ?  --->
																		No  becoz  None  is  retuned  by  default  and  None  is  not  an  iterator
'''