

#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) # Two  argument  method :  <space> 10 <space> 20
a . m1(30) #Two  argument  method :  <space>  30  <space>  2
a . m1() # Two  argument  method : <space> 1 <space> 2