# Find  outputs (Home  work)
import   time
class  Remote:
	def    __init__(self):
		self . list = ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV']
		self . index = -1
	def   __iter__(self):
		return  self
	def   __next__(self):
		self . index += 1
		if   self . index  ==  len(self . list):
			raise  StopIteration
		return    self . list[self . index]
# End  of  the  class
r = Remote() #  Object  is  initialized  with  list  =  ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV']  and  index = -1   by  constructor
for   x    in    r:
	print(x)
	time . sleep(1)


'''
Tv 9
Espn
Zee Tv
ETV
'''

#  object   'r'   --->   list =  ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV']   ,  index = -1