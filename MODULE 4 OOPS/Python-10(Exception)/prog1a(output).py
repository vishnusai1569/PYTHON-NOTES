#Find  outputs
try:
	a = eval(input('Enter  first  number : '))  #     'Ten'
	b = float(input('Enter  second  number : ')) #   3
	c = a / b
	print('Division  Result  :  ' , c)
except   ZeroDivisionError  as  msg:
	print('2nd  input  can  not  be  zero :  ' , msg)
except  (ValueError , NameError , TypeError)  as  msg:
	print('Input  can  not   be  string :  ' , msg)
except:
	print('A  new  error')


'''
1) What  is  the  issue  if  inputs  are  10  and  0 ?  --->  10 / 0  throws  ZeroDivisionError

2) What  is  the  issue  if  inputs  are  10  and  Two  ?  --->
														float('Two')  throws  ValueError  becoz  'Two'  can  not  be  converted  to  float

3) What  is  the  issue  if  input  is  Ten ? --->  eval('Ten')  throws  NameError  becoz  object  Ten  does  not  exist

4) What  is  the  result  of  eval("   'Ten'  ") ?  --->'Ten'

5) What  is  the  issue  if  inputs  are  'Ten'  and  2  ?  --->  'Ten' / 2  throws  TypeError  due  to  invalid  operand

6) except  NameError , ValueError , TypeError:
	           pass
    Is  the  above  except  suite  valid  ?  --->  No  becoz  ()  are  missing

7) except  as  msg:
	        pass
    Is  above  except  suite  valid  ?  --->  No  becoz  'as'  is  not  permitted  for  default  except

8) except  (NameError  as  msg1 , ValueError  as  msg2 , TypeError  as  msg3):
	                     pass
    Is  above  except  suite  valid  ?  --->  No  becoz  as  can  be  used  only  once  outside  the  brackets
'''