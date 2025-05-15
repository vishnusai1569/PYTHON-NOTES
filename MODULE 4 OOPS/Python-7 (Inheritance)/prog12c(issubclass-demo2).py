# Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3)) # True : c4  is  a  child  of  c3
print(issubclass(c4 , c2))  # True : c4  is  a  grand  child  of  c2
print(issubclass(c4 , c1))  # True : c4  is  a  great  grand  child  of  c1
print(issubclass(c4 , object))  # True : c4  is  a  child  of  object
print(issubclass(c4 , (int , float , str , bool))) # False :   c4 is  a  not  a  child  to  int , float , str  (or)  bool
print(issubclass(c4 , (int , float , c1 , str , bool))) # True : c4  is  a  child  of  c1
#print(issubclass(c4 , [int , float , c1 , str , bool])) #  Error :   2nd  arg   should  be  a  tuple  but  not  a  list