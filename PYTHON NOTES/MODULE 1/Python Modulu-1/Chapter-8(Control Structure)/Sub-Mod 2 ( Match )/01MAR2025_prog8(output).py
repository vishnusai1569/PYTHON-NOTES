'''
1) What  are  the  outputs  if  input  is  -6 ? --->  Hyd , Sec , Cyb , Bye
2) What  are  the  outputs  if  input  is  15  ?  --->  One  , Two , Three , Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->  India , China , Usa , Bye
4) What  are  the  outputs  if  input  is  0  ?  --->  Hyd , Sec , Cyb , Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> One  , Two , Three , Bye
6) What  are  the  outputs  if  input  is  7  ?  --->  Hyd , Sec , Cyb , Bye
'''
x = eval(input('Enter any  number :  '))
match  x:
	case  7 |  -6  |  0:
		print('Hyd')
		print('Sec')
		print('Cyb')
	case  -10 | 15:
		print('One')
		print('Two')
		print('Three')
	case  _:
		print('India')
		print('China')
		print('Usa')
# End  of  match
print('Bye')




'''
What  is  '|'  operator  called ?  --->  Bitwise  or  operator
'''
