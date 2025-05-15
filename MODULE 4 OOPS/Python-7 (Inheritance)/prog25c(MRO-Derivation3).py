# Find  outputs  (Home  work)
class  D:
        def __init__(self):
                super() . __init__()  #  Executes  constructor  of  class   E  becoz  super  of  class  'D'   is  'E'  (determined  from  A . mro())
                print('class D constructor')
class  E:
        def __init__(self):
                super() . __init__()  #  Executes  constructor  of  class   F  becoz  super  of  class  'E'   is  'F'  (determined  from  A . mro())
                print('class E constructor')
class  F:
        def __init__(self):
                super() . __init__()  #  Executes  constructor  of  class  object  becoz  super  of  class  'F'   is   object  (determined  from  A . mro())
                print('class F constructor')
class  B(D , E):
        def __init__(self):
                super() . __init__()  #  Executes  constructor  of  class   C  becoz  super  of  class  'B'   is  'C'  (determined  from  A . mro())
                print('class B constructor')
class  C(D , E , F):
        def __init__(self):
                super() . __init__()  #  Executes  constructor  of  class   D  becoz  super  of  class  'C'   is  'D'  (determined  from  A . mro())
                print('class C constructor')
class  A(B , C):
        def __init__(self):
                super() . __init__() #  Executes  constructor  of  class   B  becoz  super  of  class  'A'   is  'B'  (determined  from  A . mro())
                print('class A constructor')
#end of the class
print(A . mro())#   A , B , C , D , E , F , object
obj = A()  #  Executes  constructor  of  class  A  becoz  class  'A'   object  is  created
print('Bye')

'''
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]
class F constructor
class E constructor
class D constructor
class C constructor
class B constructor
class A constructor
Bye


A . mro = A + merge(B . mro + C . mro + BC)
            = A + merge(BDEO + CDEFO + BC)
            = A + B + merge(DEO + CDEFO + C)
            = A + B + C + merge(DEO + DEFO )
            = A + B + C + D + merge(EO + EFO)
            = A + B + C + D + E + merge(O + FO)
            = A + B + C + D + E + F + merge(O + O)
            = A + B + C + D + E + F + O
'''