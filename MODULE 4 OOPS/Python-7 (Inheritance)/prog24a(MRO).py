# Method  Resolution  Order (mro)
class  A:
        def __init__(self):
                print('class  A  constructor')
                super() . __init__()
class  B:
        def __init__(self):
                print('class  B  constructor')
                super() . __init__()
class  C:
        def __init__(self):
                print('class  C  constructor')
                super() . __init__()
class  D(C , A , B):
        def  __init__(self):
                print('class  D  constructor')
                super() . __init__()
#end of the class
print('MRO  of  class  A  :  ' , A . mro()) #   A , object
print('MRO  of  class  B  :  ' , B . mro())  #  B , object
print('MRO  of  class  C  :  ' , C . __mro__)  #  C , object
print('MRO  of  class  D  :  ' , D . __mro__)  #  D , C , A , B , object
print('MRO  of  class  object : ' , object . mro()) #  object
obj1 = D() #  Executes  5  constructors  in  the   order  D , C  , A  ,  B  and object
print()
obj2 = C()  #  Executes  2  constructors  in  the   order   C  and object
print()
obj3 = B()  #  Executes  2  constructors  in  the   order   B  and object
print()
obj4 = A()  #  Executes  2  constructors  in  the   order   A  and object
print()
obj5 = object()  #  Executes  object  class  constructor  which  is  an  empty  constructor

'''
MRO  of  class  A  :   [<class '__main__.A'>, <class 'object'>]
MRO  of  class  B  :   [<class '__main__.B'>, <class 'object'>]
MRO  of  class  C  :   (<class '__main__.C'>, <class 'object'>)
MRO  of  class  D  :   (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
MRO  of  class  object :  [<class 'object'>]
class  D  constructor
class  C  constructor
class  A  constructor
class  B  constructor
class  C  constructor
class  B  constructor
class  A  constructor
'''