# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self  #   Executes   destructor  before  object  is  deleted
	def  __del__(self):
		print('destructor')
		b = c1()  # Executes  constructor
a = c1() # Executes  constructor



'''
constructor
destructor
constructor
destructor
constructor
destructor
and  so  on
'''

'''
Finally  what  is  the  moral ?  --->  Do  not  create  object  in  constructor  and  destructor.
'''