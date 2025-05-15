# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		super() . __init__() # How  to  call  parent  class  constructor
		print('child   constructor')
	def   __del__(self):
		super() . __del__() # How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child() # Executes  constructor  of  child class
print('Bye')
#  Executes  destructor  of  child  class  before  object  'c'  is  lost

'''
parent  constructor
child   constructor
Bye
parent  destructor
child   destructor
'''