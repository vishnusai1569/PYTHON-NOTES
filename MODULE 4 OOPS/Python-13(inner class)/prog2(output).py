# Find  outputs  (Home  work)
class   Emp:
	def __init__(self):  #  self  is  object   'e'
		self . empno = 25
		self . ename = 'Rama Rao'
		self . sal = 10000.0
		self . dob = self . Date()  #   How  to  create  Date  class  object
	def   disp(self):
		print(self . empno , self . ename , self . sal , sep = '\t' , end = '\t\t')
		self . dob . disp() #   How  to  call  disp()  method  of  Date  class
	class   Date:
		def    __init__(self):  #  self  is   object  e . dob
			self . dd = 15
			self . mm = 8
			self . yy = 1947
		def disp(self):
			print(self . dd , self . mm , self . yy , sep = '-')
# End  of  the  class
e = Emp()
e . disp()  #  How  to  call  disp()  method  of Emp  class

# Output:   25 <tab>  Rama  Rao <tab>   10000.0  <tab> <tab>  15 - 8 - 1947

#  Object  'e'  --->  empno = 25  ,  ename = 'Rama  Rao' , sal = 10000.0 , dob  --->  (dd = 15 , mm = 8 , yy= 1947)


'''
1) self . dob =  self . Date()
    What   is  the  alternative  to  the  statement ?   --->  self . dob =  Emp . Date()

2) self . dob = Emp() . Date()
     What  is  the  issue  with  the  statement ?  ---> Infinite   recursion

3) dob = self . Date()
    What  is  the  issue  with  the  statement ?  --->  dob  is  a  local  object  to  constructor  and
									                                              hence  can  not  be  used  by  other  methods  of  the  class

4) self . dob = Date()
    What  is  the  issue  with  the  statement ?  ---> Inner  class  object  can  not  be  created
														                         without  outer  class  object  (or)  outer  classs  name
'''