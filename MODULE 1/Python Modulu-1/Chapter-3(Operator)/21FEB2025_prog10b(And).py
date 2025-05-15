#  and  operator  demo  program
print(True  and  False)    #  False
print(False  and  True)  #  False
print(False  and   False)  #   False
print(True  and  True)  # True
print(10  and  20)  #  20
print(0  and  20) #  0
print(-25  and  0)  #  0
print(''  and  25)  #  Empty  string
print(6j  and  'Hyd')  #  Hyd
print(0j  and  'Sec') #   0j
print('Hyd'   and  10.8)  # 10.8
print(10  and  20  and  30)  # 20  and 30  = 30


'''
and  operator
----------------
1) When  is  the  result  of  and  operator  False ?  --->  When  at  least  one  operand  is  False
    When  is  the  result  of  and  operator  True ?  --->When  both  the  operands  are  True

2) What  is  the  result  of  op1  and  op2  when  op1  is  True ?  --->  op2
    What  is  the  result  of  op1  and  op2  when  op1  is  False ?  --->	op1

3) Is  0  True  (or)  False  ?  --->  False
    What  about  Non-zero ? --->  True

4) Is  ''  True  (or)  False  ?   ---> False  due  to  empty  string
     What  about  non-empty  string ?  ---> True

5) What  is  0j  ---> False  due  to  zero  imag
    What  is  4j  --->  True  due  to  non-zero  imag
    What  is  3 + 0j ?  --->  True  due  to  non-zero  real
'''
