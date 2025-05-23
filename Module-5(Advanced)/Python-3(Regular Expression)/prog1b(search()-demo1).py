'''   (Home  work)
1) What  are  the  outputs  if  1st  input  is  'Hyd is green city'  and   2nd  input  is  'Green' ?  --->
																													class  <'re.Match'>
																													green is found between indexes 7 and 11
2) What  are  the  outputs  if  1st  input  is  'Hyd is green city'  and   2nd  input  is  'red' ?  ---> <class 'NoneType'>
																																				      red is not found
'''
import   re
string = input('Enter  any  string  :  ')
pattern = input('Enter  pattern  :   ')
m  =  re . search(pattern , string , re . IGNORECASE)
print(type(m))
if  m:
	print(F'{m . group()}  is found  between  indexes  {m . start()}   and   {m . end() - 1}')
else:
	print(pattern , ' is  not  found ')


'''
1) When  is  if  condition  True ?  --->  When  search()  function  returns  Match  object  which  is  a  non-empty  object

2) When  is  if  condition  False ?  --->   When  search()  function  returns  None  which  is  nothing  but  False
'''