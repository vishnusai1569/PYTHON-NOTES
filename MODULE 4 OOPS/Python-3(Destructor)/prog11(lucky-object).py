
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
   #Object  'a'  is  not  lost  becoz  there is  global  ref 'b'  to  the object
a = c1()
del  a   #  Executes  destructor  before  object  'a'  is  lost
print('Hello')
#  Destructor  is  not  executed  before    object  'b'  is  lost   becoz  it  is already executed


'''
Destructor
Hello
'''

'''
1) Why  is  destructor  executed  for  del   a  ? --->  Since  it  deletes  ref  'a'

2) When  is  global  ref  'b'  lost ?  --->  Soon  after  program  terminates

3) Why  is  destructor  not  executed  when  ref  'b'  is  lost ?  --->  Since  it  is  already  executed  when   ref  'a'  is  deleted

4) Finally, how  many  times  destructor  is  executed  for  an  object ?  --->  Just  once
'''