# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())  #  False  due  to  '$'
print('Hyd' . isdigit())  #  False  due  to  'H'
print('+-$' . isdigit())  #  False  due  to  '+'
print('A2#' . isdigit())  #  False  due  to  'A'
print('' . isdigit())  #  False  due  to  no  digits
print(' ' . isdigit())  #  False  due  to  ' '
#print(9247 . isdigit())  #  Error  becoz  there  is  ni  isdigit()  method  in int  class



'''
isdigit()  method
--------------------
1) When  does  it  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  non-digit(i.e. alphabet  (or) special  character)
																					   (or)
															  When  there  are  no  digits  in  the  string
'''
