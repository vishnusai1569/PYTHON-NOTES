# Identify  the   issue ?
x = bool(input('Enter  Boolean  input  :  '))
print(type(x))
print(x)



'''
Input           input()  reads     bool(input())  returns
--------------------------------------------------------------------------
 True                   'True'            bool('True')  is  True
 False				    'False'           bool('False')  is  True  becoz  'False'  is  a  non-empty  string
 <Enter key>         ''                   bool('')  is  False
 25					    '25'               bool('25')  is  True  becoz   '25'  is  a  non-empty  string
 10.8                    '10.8'             bool('10.8')  is  True  becoz  '10.8'  is  a  non-empty  string
 Hyd					    'Hyd'             bool('Hyd')  is  True
 <Space  bar>	    ' '                  bool(' ')  is  True  becoz  ' '  is  a  non-empty  string
-----------------------------------------------------------------------------------
1) What  is  the  issue  with  bool(input()) ?  --->  Reads  True  for  every  input  except  for  enter  key

2) How  to  overcome  this  issue ? ---> With  eval(input())

3) Why  are  try  and  except  not  used  in  the  above  program ? --->
																						No  error  is  reported  even  when  input  is  not  boolean
'''
