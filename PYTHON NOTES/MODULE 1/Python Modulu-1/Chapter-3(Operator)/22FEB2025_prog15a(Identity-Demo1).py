# Identity operators demo program
a = 25
b = 25
print(a is b) #   True
print(a is not b)  #   False
print(a == b) #  True



'''
Identity    operators
-------------------------
1) What  are  the  two  identity  operators ? --->  is  and  is  not

2) What  does  ref1  is  ref2  do ?  --->  Compares  references
     What  does   ref1 == ref2  do ?  ---> Compares  objects  pointed  by  ref1  and  ref2

3) What  is  the  result  of  ref1  is  ref2 ?  --->
														True  when  both  the  references  point  to  same  object  and  False  otherwise
    What  is  the  result  of  ref1  ==  ref2 ?  --->
	                                                             True  when  both  the  objects  have  same  value  and  False  otherwise

4) is  and  is  not  are  quite  opposite  operators
'''
