#  Identify  Error
class  c1:
	pass
# End of the class
a = c1()
b = c1()
#print(a + b) #  Error : No  __add__()  method  in  class  c1
#print(a - b)  #  Error : No  __sub__()  method  in  class  c1
#print(a * b)   #  Error : No  __mul__()  method  in  class  c1
#print(a / b)  #  Error : No  __truediv__()  method  in  class  c1
#print(a // b) #  Error : No  __floordiv__()  method  in  class  c1


'''
1) Which  method  is  executed  for  10 + 20  and  what  is  the  result ?  --->
														__add__()  method  of  int  class  is  executed  and  the  result  is  30

2) Which  method  is  executed  for  '10' + '20'   and  what  is  the  result ?  --->
														__add__()  method  of  str  class  is  executed  and  the  result  is   '1020'

3) Which  method  is  executed  for  [10 , 20 , 30] + [40 , 50 , 60]  and  what  is  the  result ?  --->
							__add__()  method  of  list  class   is  executed  and  the  result  is  [10 , 20 , 30 , 40 , 50 , 60]
'''