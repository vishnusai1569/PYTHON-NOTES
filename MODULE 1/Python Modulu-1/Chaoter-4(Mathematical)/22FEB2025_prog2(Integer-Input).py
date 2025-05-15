# How  to  read  an  integer  input ?  --->  int(input())
try:
	x = int(input('Enter  any   integer  number  :  ' , ) )
	print(type(x))
	print(x)
except:
	print('Input  should  be  integer')


'''
Input     What  does  input()  read      What  does  int(input())  return
---------------------------------------------------------------------------------------
  25                          '25'                               int('25')  is  25
  10.8					    '10.8'                            int('10.8')  throws  error
  True					    'True'                           int('True')  throws  error
  Ten						    'Ten'                             int('Ten')   throws  error
  3 + 4j					    '3+4j'                            int('3+4j')  throws  error
------------------------------------------------------------------------------------------
1) What  is  the  result  of  int(10.8)  ?  --->  10
    What  is   the  result  of  int('10.8')  ?  ---> Error  due  to  string  float

2) What  is  the  result  of  int(True) ?  --->  1
    What  is  the  result  of  int('True') ?  --->	Error  due  to  string  boolean

3) except:
	     stmt1
	     stmt2
	     stmt3
    Is  the  above  except  valid ?  ---> No  becoz  except  can  not  be  used  without  try

4) try:
	     stmt1
	     stmt2
	     stmt3
   Is  the  above  try  valid  ?  --->  No  becoz  try  can  not  be  used  without  except

5) In  other  words,  try  and  except  form  a  pair

6) try:
    stmt1
    except:
    stmt2
    Is  the  above  code  valid ?  ---> 	No  becoz  spacebar (or) tab  is  required  before  stmt1  and  stmt2  due  to
									                    colon  after  try  and  except

7) In  other  words,  at  least   one  space  bar  (or)  tab  is  mandatory  after  :

8) What  is  the  advantage  of  try  and   except  suites ? --->  Error  is  not  reported  and  user  friendly  msg  is  printed
'''
