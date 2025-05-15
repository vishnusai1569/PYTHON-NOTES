#  Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4:
        pass
#  End  of  the  class
print(isinstance(25 , int)) # True :  25 is  an  int  class  object
print(isinstance(10.8 , float))  # True :  10.8  is   a   float   class  object
print(isinstance('Hyd' , str))  # True :  'Hyd'  is   a   str  class  object
print(isinstance(3 + 4j , complex))  # True :  3+4j  is  a  complex  class  object
print(isinstance(True , bool))  # True :  True  is   a   bool   class  object
print(isinstance(True , int))  # True :  True  (or) 1   is   an  int  class  object
print(isinstance('True' , str))  # True :  'True'  is   a   str  class  object
print(isinstance(True , str)) # False :  True  is   not  a   str  class  object
print()
a = c3()
print(isinstance(a , c3))  # True :  'a'  is   c3  class  object
print(isinstance(a , c2))  # True :  'a'  is   c3  class  object  but  c3  extends  c2
print(isinstance(a , c1))   # True :  'a'  is   c3  class  object  but  c3  extends  c2  and  c2  extends  c1
print(isinstance(a , object))   # True :  'a'  is   c3  class  object  but  c3  extends  object
print(isinstance(a , c4))  # False :  'a'  is   c3  class  object  but  c3  does  not  extend   c4
print(isinstance(a , (int  ,  float  ,  str  ,  bool)))   # False :  'a'  is   c3  class  object  but  c3  does  not  extend   int , float , str  and  bool
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool)))   # True :  'a'  is   c3  class  object
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool)))   # True :  'a'  is   c3  class  object  but  c3  extends  c2  and  c2  extends  c1
#print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool])) # Error :  2nd  arg  should  be  a  tuple  but  not  list