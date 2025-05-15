# Find  outputs(Home  work)
class   c1:
	def   __init__(self): #  self  is  object  'a'
		self . x =  1   #  Adds  variable  'x'  to  object  'a'  with  value  1
	def   __iter__(self):
		print('__iter__    method')
		return  self
	def   __next__(self):
		value =  self . x
		self . x  +=  1
		return  value
# End  of  the  class
a = c1() #  Object  is  initialized  with  x = 1  by  constructor
print('Elements  of  iterator  with  for  loop')
for   element   in   a:  #  Executes  __iter__()  and  __next__()  methods  in  1st  iteration  and  only  __next__()  method  in  subsequent  iterations
	print(element)
	if  element  ==  5:
               break
print('Elements  of  iterator  with  next()  function')
while    True:
	element = next(a)
	print(element)
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop')
for   element   in    a:  #  Executes  __iter__()  and  __next__()  methods  in  1st  iteration  and  only  __next__()  method  in  subsequent  iterations
	print(element)
	if  element  ==  15:
		break


'''
Elements  of  iterator  with  for  loop
__iter__    method
1
2
3
4
5
Elements  of  iterator  with  next()  function
6
7
8
9
10
Elements  of  iterator  with  for  loop
__iter__    method
11
12
13
14
15
'''

'''
1) Is  c1  a  finite  iterator  ?  --->  No  becoz  __next__()  method  is  not  raising  StopIteration  error

2) Is  if  condition  mandatory  in   for  loop  and  while  loop ?  --->  Yes

3) What  happens  when  if  condition  is  omitted ?  --->  Infinite  loop
'''