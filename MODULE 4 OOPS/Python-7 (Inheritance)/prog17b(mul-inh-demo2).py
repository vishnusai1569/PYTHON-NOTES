# Find  outputs
class  uncle:
        def  m1(self):
                print('uncle  Method')
class  mother:
        def  m1(self):
                print('mother  Method')
class  father:
        def  m1(self):
                print('father  Method')
class  child(father , mother , uncle):
	pass
#end  of  the  class
c = child()
c . m1()  #  Method  of  father  class  is  executed  becoz   there  is  no  m1()  in   child  class  i.e.  father  Method


'''
Classes  derivation  order  matters  but  not  classes  definitions  order
'''