'''  (Home   work)
1) What  are  the  outputs  if  inputs  are  'HYD'  and  'hyd' ?  --->  Same  strings  after  ignoring  the  case

2) What  are  the  outputs  if  inputs  are  'HYD'  and  'SEC' ?  --->  Different  strings
'''
import  re
s1 = input('Enter first string  : ')
s2 = input('Enter second string  : ')
m  = re . fullmatch(s1 , s2 , re . IGNORECASE)
if  m:
        print('Same  strings  after  ignoring  the  case')
else:
        print('Different  strings')