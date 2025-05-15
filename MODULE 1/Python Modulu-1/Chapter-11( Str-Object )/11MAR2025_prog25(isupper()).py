# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper()) #   False  becoz  there  are  no  uppercase  alphabets
print('RAMA  RAO' . isupper())  #  True  becoz  there  are  no  lowercase  alphabets
print('+-$' . isupper())  #   False  becoz  there  are  no  uppercase  alphabets
print('HYD123' . isupper())   #  True  becoz  there  are  no  lowercase  alphabets
print('HYD+-$' . isupper())   #  True  becoz  there  are  no  lowercase  alphabets
print('' . isupper())   #   False  becoz  there  are  no  uppercase  alphabets
print('A2#' . isupper())   #  True  becoz  there  are  no  lowercase  alphabets




'''
isupper()  method
----------------------
1) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  lowercase  alphabet
																								(or)
															 When  there  are  no  uppercase  alphabets  in  the  string

2) When  does  it  return  True ?  --->  When  there  are  no  lowercase  alphabets  in  the  string
																						and
															 at  least  one  character  is  an  uppercase  alphabet
'''
