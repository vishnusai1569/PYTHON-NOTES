# Find  outputs
class   A:
        def m1(self):
                print('Method  of  class  A')
                #super() . m1()  #  Error :  No  m1()  method  in  class  object  as  super()  of  A  is  object (determined  from  D . mro())
class  B(A):
        def m1(self):
                print('Method  of  class  B')
                super() . m1()  #  Executes  method  of  class  C  becoz   super()  of  B  is  C  (determined  from  D . mro()  is   D , B , C , A  , object)
class  C(A):
        def m1(self):
                print('Method  of  class  C')
                super() . m1()  #  Executes  method  of  class  A  becoz   super()  of  C  is   A  (determined from   D . mro()  is   D , B , C , A  , object)
class  D(B , C):
        def m1(self):
                print('Method  of  class  D')
                super() . m1()  #  Executes  method  of  class  B  becoz    super()   of  D  is  B  (determined  from   D . mro()  is   D , B , C , A  , object)
#end of the class
print('MRO  of  class  object  :  ' , object . mro())  #  object
print('MRO  of  class  A  : ' , A . mro())  #   A , object
print('MRO  of  class  B  : ' , B . mro())  #B ,  A  , object
print('MRO  of  class  C  : ' , C . __mro__)  #  C , A , object
print('MRO  of  class  D  : ' , D . __mro__)  #  D , B , C , A , object
obj = D()
obj . m1()  #  Executes  method  of  class  D   becoz  obj  is  class  D  object
print('Bye')


'''
D . mro()  =  D + merge(B . mro() + C . mro() + BC)
               =   D + merge(BAO + CAO + BC)
               =   D + B + merge(AO + CAO + C)
               =   D + B + C + merge(AO + AO)
               =   D + B + C + A + merge(O + O)
               =   D + B + C + A + O
			   = D , B , C , A , O




1) When  is  derivation  needed  for  MRO ?  ---> When  there  is  at  least  one  grand  parent  class

2) Which  class  in  the  above  program  has  grandparent  ?  --->  class D  becoz  it  has  grand  parent  A

3) What  is  the  head  (or)  first  element  in  ABCD  ?  ---> A
     What  is  the  tail  list  in  ABCD ?  ---> BCD

4) When  is  the  head  element  selected  for  MRO ?  --->  When  it  is  not  in  tail  list  of  the  remaining

5) What  is  the  next  event  after  head  element  is  selected ?  --->  Remove  that  element  from  all  the  lists

6) What  action  to  be  made  when  head  element  is  in  tail  list  of  the  remaining ?  --->
																															Ignore  it  and  proceed  to  the  next  list
'''