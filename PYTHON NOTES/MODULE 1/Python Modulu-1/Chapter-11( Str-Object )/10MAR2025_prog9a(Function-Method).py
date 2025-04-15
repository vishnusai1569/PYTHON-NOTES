#  Difference  between  function   and   method
class    c1:
	def   m1(hyd):   #  self   is   object  'a'
		print('Method1')

	def m1(self):  # self   is   object  'a'
			print('Method2')
# End  of  the  class
def   f1():
	print('Function')
# End  of  the  function
a = c1()  #   Creates  c1  class  object   'a'
a . m1()
#f1()
f1()
#a . f1()  # Error  becoz  there  is  no  method  f1()  in  class  c1
#m1(a)    # Error  becoz  there  is  no  function  m1()  in  current  module
