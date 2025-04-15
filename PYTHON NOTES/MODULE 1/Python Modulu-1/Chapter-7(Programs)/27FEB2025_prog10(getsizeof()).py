#  getsizeof()   function  demo  program
import  sys
print(sys . getsizeof(25))  #  size  of  int  object
print(sys . getsizeof(10.8))  #  size  of  float  object
print(sys . getsizeof(3 + 4j))  #  size  of  complex  object
print(sys . getsizeof('Rama  Rao'))  #  size  of   str  object
print(sys . getsizeof(True))  #  size  of  bool object
print(sys . getsizeof(None))  #  size  of  None  object
print(sys . getsizeof([10 , 20 , 15 , 18]))  #  size  of  list  with  4  elements
#print(getsizeof(()))  #  Error  becoz  there  is  no  getsizeof()  function  in  current  module


'''
getsizeof()  function
------------------------
1) What  does  getsizeof(object)  do ?  --->  Returns  size  of  any  python  object  in  the  form  of  bytes

2) Where  is  getsizeof()  function  defined ?  --->  In  sys  module
'''
