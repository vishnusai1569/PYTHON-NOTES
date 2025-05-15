#  Which  of  the  following  statements  throw  TypeError ?  (Home  work)
print(10 + 20) #    30
print('10' + '20')  #  1020
#print(10 + '20') # TypeError :   10  and  '20' are  invalid  operands  for  '+'
print(len('25'))  #  2
#print(len(25)) # TypeError  :  25  is  an    invalid  arg   to   len()  function
s = {10 , 20 , 15 , 18}
#print(s[0]) # TypeError :  0  is  invalid  operand   for  set  's'  as  set  is  not  indexed
#b = { [10 , 20] : [30 , 40] } #  TypeError :  key  can  not  be  mutable  object  such  as  list
#print(int(3+4j)) # TypeError :  3+4j  is  an  invalid  arg  to  int()  function
#print(int([10,20,30])) # TypeError :   list  is  an  invalid  arg  to  int()  function
#print(float(None)) # TypeError  :   None  is  an  invalid  arg  to   float()  function


'''
When  is  TypeError  raised ? --->  When  the  operands  are  illegal  in  an  expression
																			            (or)
													    when  an  illegal  argument  is  passed  to  function (or)  method
'''