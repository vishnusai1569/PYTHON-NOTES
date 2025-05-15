# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	pass
# End of the class
c = child()  #  Executes  constructor  of  parent  classs  becoz  there  is  no  constructor  in  child  class
print('Bye')
#  Executes  destructor  of  parent  classs   before  object  'c'  is  lost


'''
parent  constructor
Bye
parent  destructor
'''