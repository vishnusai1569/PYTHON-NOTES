# Identify  Error  (Home  work)
class   c4:  #   c4  is  iterable  but  not  iterator
	def  __iter__(self):
		print('__iter__  method ')
		return   self #  Error  :  itr  is not  an  iterator
# End  of  the  class
itr = c4()  #  Empty  object
for  x  in   itr:  #   Valid  :   itr is  iterable
	print(x)


'''
What  is  the  issue  with  return  self  in   __iter__()  method ?  --->  self  (i.e.  object  itr)  is  not  an  iterator
																										       becoz  there  is  no  __next__()  method  in  class c4
'''