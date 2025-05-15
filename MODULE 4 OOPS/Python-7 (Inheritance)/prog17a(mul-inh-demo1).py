#  Find  outputs
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
        def  m1(self):
                print('child  Method')
#end  of  the  class
c = child()
c . m1() #  Method  of  child  class  is  executed  becoz  'c'  is  child  class  object  i.e.  child  Method