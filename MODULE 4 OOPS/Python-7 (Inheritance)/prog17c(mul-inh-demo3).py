# Find  outputs
class  uncle:
        def  m1(self):
                print('uncle  Method')
class  mother:
        def  m1(self):
                print('mother  Method')
class  father:
        pass
class  child(father , mother , uncle):
        pass
#end  of  the  class
c = child()
c . m1()  #  Method  of  mother  class  is  executed  becoz   there  is  no  m1()  in   child  and  father  classes  i.e.  mother  Method