# Find  outputs  (Home  work)
class  parent:
	def  marriage(self):
		print('Arranged Marriage')
	def  property(self):
		print('One  Crore')
	def  study(self):
		print('Studies only' , end = '\t')
class  child(parent):
	def  marriage(self):
		print('Love Marriage')
	def  study(self):
		super() . study()   #  Executes  method  of  parent  class  due  to  super()
		print(' + Entertainment')
#end of the class
c = child()
c . marriage()   #  Executes  method  of  child  class  as  'c'  is  child  class  object
c . property()    #  Executes  method  of  parent  class  as  there  is  no  property()  method  in  child  class
c . study()    #  Executes  method  of  child  class  as  as  'c'  is  child  class  object

'''
Love Marriage
One  Crore
Studies only     + Entertainment


1) Which  method  is  inherited  from  parent  class ?  --->
															Only  property()  method  becoz  it  is  not  overridden  by  child  class

2) Why  are  marriage()  and  study()  methods  not  inherited ?  --->
																						Since  they  are  overridden  by  child  class
'''