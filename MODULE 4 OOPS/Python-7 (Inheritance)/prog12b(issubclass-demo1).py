# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1)) # True : c2  is  a child  class  of  c1
print(issubclass(int , float)) # False :  int  is  not  a  child  class  of  float
print(issubclass(str , object)) # True : str is a  child  class  of  Object
print(issubclass(c1 , object)) # True :  c1  is a  child of  object
print(issubclass(c2 , object)) # True :  c2  is a  child  (or) grand child  of  object
a = c1()
b = c2()
#print(issubclass(b , a)) # Error  :  1st argument  should  be  a  class  but  'b'  is  an  object
#print(issubclass(c2 , a)) # Error  :  2nd argument  should  be  a  class  but  'a'  is  an  object