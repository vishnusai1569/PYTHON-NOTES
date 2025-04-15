# sqrt()  function  demo  program
import  math
print(math . sqrt(25))  #  5.0
print(math . sqrt(10))  # 3.16
print(math . sqrt(6.25))  #  2.5
print(math . sqrt(True))  #   1
#print(math . sqrt(3+4j))  #   Error  due  to  complex  number
print(math . sqrt(math . sqrt(256)))  #  math . sqrt(16.0) = 4.0
print(math . sqrt(math . pow(3 , 4)))    #  math . sqrt(81.0) = 9.0
#print(math . sqrt(-16))  #  Error  due  to  -ve  argument
#print(sqrt(49))  # Error


'''
1) math . sqrt(x)
    Where  is  sqrt()  function  searched ?  ---> In  math  module

2) sqrt(x)
    Where  is   sqrt()  function  searched ? ---> In  current  module  (or)  program
'''
