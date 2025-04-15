# F   string  demo  program
x = 25
print(F'{x}')  # Converts  object   'x'  to  string  i.e.  '25'
print(F'x')  #   'x'  itself  becoz  'x'  is  not  in  { }
print('{x}')  # {x}
print('x')  #  x
print(x) #  Value  of  object  'x'  i.e.  25
print(F'x = {x}')  #   x = 25
print(F'{x = }')  #   x = 25
print(f'x =')  #  x =
print(F'x : {x}') #  x : 25
print(F'{x:}')  #  25  and  :  is  ignored



'''
1) What  does  F  string  do ?  --->  Converts  any  python  object  to  string

2) What  is  the  syntax  of  F  string ?  --->  F'{object}'

3) What  does  F'{object}'  do ?  ---> Converts  object  to  string

4) What  does  F  stands  for  --->  Format  string

5) Are  F   and   f   same  ?  --->  Yes

6) How  to  obtain  object  name  and   value  of  object  with  F  string ?  --->  F'{object=}'

7) What  are  the   three  ways  to  convert  object  to  string ?  --->  str(object)  ,  '%s'  %object  ,  F'{object}'

8) What  is  the  difference  between  eval()  function  and  F  string ?  ---
														 eval()  function  converts  string  to  any  python  object  but
														 F '{object}'  converts  object  to string
'''
