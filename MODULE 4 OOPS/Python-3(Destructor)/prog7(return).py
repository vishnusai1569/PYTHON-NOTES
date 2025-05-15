# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__()) #  object  'a'  is  alive  after execution  of  destructor
print('Hello')
del   a  #  Executes  destructor   before  object  'a'  is  deleted


'''
destructor
25
Hello
destructor
'''

'''
print(del   a)
What  is  printed ?  --->   Error  becoz  del  operator  can  not  be  used  in  print()  function
'''