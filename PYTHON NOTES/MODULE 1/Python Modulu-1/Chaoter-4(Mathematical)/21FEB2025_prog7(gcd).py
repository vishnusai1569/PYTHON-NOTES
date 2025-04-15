# gcd()  function  demo  program
import  math
print(math . gcd(12 , 15))  #  3
print(math . gcd(12 , 18))  #  6
print(math . gcd(4 , 7))  #  1
print(math . gcd(7 , 7))  #  7
print(math . gcd(-18 , -27))  # 9
print(math . gcd(-4 , 6))  #  2
print(math . gcd(0 , 7))  #   7  becoz  1st  arg  is  0
print(math . gcd(3 , 0))  #   3  becoz   2nd  arg  is  0
print(math . gcd(0 , 0))  #  0
#print(gcd(5 , 15)) #  Error  becoz  there  is  no  gcd()  function  in  current  module


'''
1) Does  gcd()  function  return  -ve  result ?  --->  No  even  though  arguments  are  -ve

2) What  is  the  result  of  gcd  when  an  argument  is  0 ?  --->  Other  argument
'''
