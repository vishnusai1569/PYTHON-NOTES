# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())#False
print('Hyd' . isdigit())#False
print('+-$' . isdigit())#False
print('A2#' . isdigit())#False
print('' . isdigit())#flase
print(' ' . isdigit())#False
#print(9247 . isdigit())#ERROR method not define



'''
isdigit()  method
--------------------
1) When  does  it  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  alphabet  (or) special  character
																					   (or)
															  When  there  are  no  digits  in  the  string
'''