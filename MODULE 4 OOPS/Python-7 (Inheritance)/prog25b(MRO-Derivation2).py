# Find outputs  (Home  work)
class  A:
	def  m1(self):
		super() . m1()    #  Method  of  class  Y  is  executed   becoz   super   of  class   A  is   Y (determined  from  P . mro())
		print('class A method')
class  B:
	def m1(self):
		super() . m1()    #  Method  of  class   C   is  executed   becoz   super   of  class   B   is   C (determined  from  P . mro())
		print('class B method')
class  C:
	def m1(self):
		super() . m1()    #  Method  of  class   D  is  executed   becoz   super   of  class   C   is    D  (determined  from  P . mro())
		print('class C method')
class  D:
	def m1(self):
		#super() . m1()  #  Error :    #   No  m1()  method   in  object   class   as  super   of  class   D  is   object (determined  from  P . mro())
		print('class D method')
class  X(A , B):
        def m1(self):
                super() . m1()    #  Method  of  class  A  is  executed   becoz   super   of  class   X   is   A (determined  from  P . mro())
                print('class X method')
class  Y(B , C , D):
        def m1(self):
                super() . m1()    #  Method  of  class  B   is  executed   becoz   super   of  class   Y   is    B (determined  from  P . mro())
                print('class Y method')
class  P(X , Y , C):
        def m1(self):
                super() . m1()   #  Method  of  class  X  is  executed   becoz   super   of  class  P  is   X (determined  from  P . mro())
                print('class P method')
#end of the class
print(P . mro()) #    P , X , A , Y , B , C , D , object
obj = P()
obj . m1()  #  Method  of  class P  is  executed   becoz  obj  is  class  'P'  object
print('Bye')


'''
[<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>]
class D method
class C method
class B method
class Y method
class A method
class X method
class P method
Bye



1) Is  derivation  needed  for  P . mro() ?  --->  Yes  becoz  'P'  has   grand  parent  classes   A , B , C  and  D

2) P . mro() =   P + merge(X . mro() + Y . mro() + C . mro() + XYC)
			      =   P + merge(XABO + YBCDO + CO + XYC)
			      =   P + X + merge(ABO + YBCDO + CO + YC)
			      =   P + X + A + merge(BO + YBCDO + CO + YC)
			      =   P + X + A + Y + merge(BO + BCDO + CO + C)
			      =   P + X + A + Y + B + merge(O + CDO + CO + C)
			      =   P + X + A + Y + B + C + merge(O + DO + O)
			      =   P + X + A + Y + B + C + D + merge(O + O + O)
			      =   P + X + A + Y + B + C + D + O
			      =   P , X , A , Y , B , C , D , object
'''