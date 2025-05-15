# Find  outputs  (Home  work)
try:
	print(7 / 0)  # Throws   ZDE
except   ArithmeticError:  #   Caught  becoz  ArithmeticError  is  parent  to  ZDE
	print('Arithmetic Error')  #  Arithmetic  Error
except   ZeroDivisionError:  #  Not  executed  becoz  1st  except  suite  is  already  execute d
	print('Zero Division  Error')
print('End') #  End


'''
1) What  is  ArithemeticError ?  --->  Parent  class  to  ZeroDivisionError

2) What  happens  when  parent  error  is  handled  before  child  error ?  --->
																		Parent  error  is  executed  even  though  child  error  is  raised

3) In  other  words,  errors  can  be  handled  in  any  order  (only  in  python)
'''