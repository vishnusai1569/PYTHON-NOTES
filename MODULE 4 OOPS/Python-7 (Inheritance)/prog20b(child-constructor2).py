# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		print('child   constructor')
	def   __del__(self):
		print('child  destructor')
# End of the class
c = child()  #  Executes  constructor  of  child  class
print('Bye')
#  Executes  destructor  of   child  class  before  object  'c'  is lost

'''
child   constructor
Bye
child  destructor
'''


'''
Why  are  parent  class  constructor  and  destructor  not  executed ?  --->
														Since  they  are  not  called  by  child  class  constructor  and  destructor
'''