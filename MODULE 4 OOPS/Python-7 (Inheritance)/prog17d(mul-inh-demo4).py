# Find  outputs
class  uncle:
        def  m1(self):
                print('uncle  method')
class  mother:
        pass
class  father:
        pass
class  child(father , mother , uncle):
        pass
#end  of  the  class
c = child()
c . m1() #  Method  of  uncle  class  is  executed  becoz   there  is  no  m1()  in   child ,  father  and  mother  classes  i.e.  uncle  Method