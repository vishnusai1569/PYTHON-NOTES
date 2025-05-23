#  Identify  Error  (Home  work)
import re
string  =  input('Enter  any  string : ')
pattern = input('Enter  any pattern : ')
m  =  re . match(^pattern , string , re . IGNORECASE) # Error :  '^'  demands   string   but  not string object
if  m:
	print(string  ,  'starts  with ' , m . group())
else:
	print(string , 'does not start with' , pattern)


'''
m  =  re . match(^pattern , string , re . IGNORECASE)
What  is  the  alternative  to  the  statement ?  --->  m  =  re . match('^' + pattern , string , re . IGNORECASE)
'''