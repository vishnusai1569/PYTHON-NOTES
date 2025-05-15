
# Find  outputs (Home  work)
class    c1:  #  Discarded  becoz  a  function  is  defined  with  same  name later
	def   __init__(self):
		print('Constructor')
def  c1():  #   Recognized
	print('Function')
#end of the  class
a = c1()  #  Executes  function  c1()  which  returns  None   by  default
print(a)  # None

'''
Function
None
'''