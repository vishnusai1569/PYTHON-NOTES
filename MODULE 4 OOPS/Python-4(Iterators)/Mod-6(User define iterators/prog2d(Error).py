# Identify  Error
class   c5:#   c5  is  iterable  but  not  iterator
	def  __iter__(self):
		print('__iter__  method ')   #  Error  :  None  is  not  an  iterator
# End  of  the  class
itr = c5() #  Empty  object
for  x  in   itr:#   Valid :  itr  is  iterable
	print(x)