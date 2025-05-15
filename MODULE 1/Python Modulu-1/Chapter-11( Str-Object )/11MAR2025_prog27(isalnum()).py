# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum())  #  False  due  to   '+'
print('hyd' . isalnum())  #  True  becoz  there are  no  special  chars
print('hYd' . isalnum())  #  True  becoz  there are  no  special  chars
print('9247' . isalnum())  #  True  becoz  there are  no  special  chars
print('' . isalnum())  #  False  becoz  there  is  no  alphabet  nor  digit
print('A7g9'  . isalnum())  #  True  becoz  there are  no  special  chars



'''
isalnum()  method
----------------------
1) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  speical  character
																						(or)
															  when  there  are  no  alphabets  (or)  digits

2) When  does  it  return  True ?  --->  When  there  are  no  special  characters  in  the  string

3) What  is  isalpha()  +  isdigit()  called ?  --->  isalnum()
'''
