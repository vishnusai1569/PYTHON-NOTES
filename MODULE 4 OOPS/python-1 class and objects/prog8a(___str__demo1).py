prog8a(___str__demo1).py

#  Find  outputs  (Home  work)
class  Date:
	def   disp(self):   #  self   is  object  'a'
		print('dd : ' , self . dd)
		print('mm : ' , self . mm)
		print('yy : ' , self . yy)
	def  __str__(self):  #  self  is  object  'a'
		return  F'{self . dd}-{self . mm}-{self . yy}'
#end of the class
a =  Date()   #  Creates  an  empty  Date  class  object
a . dd = 15  # Adds  3  variables  to  object    'a'  with  values  15 , 8  and  1947
a . mm = 8
a . yy = 1947
a . disp()
print(a)  #  print('15-8-1947')
print(a . __str__())  #  print('15-8-1947')
print(a . __dict__)  #   {'dd' : 15 , 'mm' : 8 , 'yy' : 1947}



'''
# object  'a'  --->   dd = 15 , mm = 8 , yy = 1947



1) How  to  print  object  in  dictionary  form ?  --->  print(object . __dict__)

2)	How  to  print  object  in   string  form ?  --->  print(object)
																				  (or)
																			 print(object . __str__())

3) How  to  print  object  in  object  form ?  --->  object . disp()
'''