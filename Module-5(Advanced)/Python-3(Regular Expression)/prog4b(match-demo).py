''' (Home  work)
1) What  are  the  outputs  if  1st  string  is  'Sankar  dayal  sarma'  and  2nd  string  is  'san'   ?  --->
																															Sankar dayal sarma starts with San

2) What  are  the  outputs  if  1st  string  is  'Hyderabad'  and  2nd  string  is  'Sec' ?  --->
																														Hyderabad does not start with Sec
'''
import re
string  =  input('Enter  any  string : ')
pattern = input('Enter  any pattern : ')
m  =  re . match(pattern , string , re . IGNORECASE)
if  m:
	print(string  ,  'starts  with ' , m . group())
else:
	print(string , 'does not start with' , pattern)


'''
1) When  is  if  condition  True ? --->  When  match()  function  returns  Match  object  which  is  a  non-empty  object

2) When  is  if  condition  False ? --->  When  match()  function  returns  None  which  is  treated  as  False  in  the  condition
'''