#  //  operator  demo  program
print(9 // 2)    #  4
print(9.0 // 2)  #   prev  integer  of   4.5  =  4.0
print(9 // 2.0)  #   prev  integer  of   4.5  =  4.0
print(9.0 // 2.0)   #  prev  integer  of   4.5  =  4.0
print(10.5 // 2)#  prev  integer  of    5.25  =  5.0
print(10 // 3)  #  3
print(10.0 // 3)  #  prev  integer  of   3.33  =  3.0
print(8.5 // 3)  # prev  integer  of   2.8  =  2.0
print(18 // 4)    #   4
print(-18 // 4)  #  prev  integer  of   -4.5  =   -5
print(-(18 // 4)) #  -4



'''
//  operator
--------------
1) What  is  the  result  of  integer // integer ?  --->  Integer  quotient
    What  is  the  result  of  integer // float ?  --->  Float  quotient  with  .0
    What  is  the  result  of  float // integer ?  ---> Float  quotient  with  .0
    What  is  the  result  of  float // float ?  --->  Float  quotient  with  .0

2) What  is  the  result  of  integer / integer ?  --->   Float  quotient
    What  is  the  result  of  integer / float ?  --->  Float  quotient
    What  is  the  result  of  float / integer ?  --->  Float  quotient
    What  is  the  result  of  float / float ?  --->  Float  quotient

3) What  does  /  operator  do ?  --->  Performs  division  and  returns  float  quotient
     What  does  //  operator do ?  --->  Performs  division  and  returns  integer  quotient

4) When  is  the  result  of  //  operator  integer ?  --->  When  both  the  operands  are  integers
    When  is  the  result  of   //  operator  float  with  .0 ?  --->When  at  least  one  operand  is  float
'''
