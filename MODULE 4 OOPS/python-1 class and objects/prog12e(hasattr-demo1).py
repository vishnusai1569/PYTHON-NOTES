

#  Find  outputs  (Home  work)
class   rat:
	def    m1():
		pass
# End  of  the  class
a = rat() #  Empty  object
a . nr = 22  # Adds  variable  nr  to  object  'a'  with   value  22
print(hasattr(a , 'nr')) #   True : Variable  'nr'  exists  in  object  'a'
print(hasattr(a , 'dr'))  #   False : Variable  'dr'  does  not  exist  in  object  'a'
print(hasattr(a , 'm1'))  #   True :  Method  'm1'  exists  in  class   rat
print(hasattr(a , 'm2'))  #  False :  Method  'm2'  does  not  exist  in  class   rat
print(hasattr(rat , 'm1'))  #   True :  Method  'm1'  exists  in  class   rat
print(hasattr(rat , 'm2'))  #  False :  Method  'm2'  does  not  exist  in  class   rat
print(hasattr(rat , 'nr'))   #  False :  Method  'nr'  does  not  exist  in  class   rat