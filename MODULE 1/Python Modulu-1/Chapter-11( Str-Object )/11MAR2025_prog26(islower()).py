# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower())  #  False  becoz  there   are  ni  lowercase  alphabets
print('rama  rao' . islower())   #  True  becoz  there  are  no  uppercase  alphabets
print('+-$' . islower())  #  False  becoz  there   are  ni  lowercase  alphabets
print('hyd+-$' . islower())    #  True  becoz  there  are  no  uppercase  alphabets
print('abc123' . islower())    #  True  becoz  there  are  no  uppercase  alphabets
print('' . islower())   #  False  becoz  there   are  ni  lowercase  alphabets
print('a2#' . islower())      #  True  becoz  there  are  no  uppercase  alphabets


'''
islower()  method
---------------------
1) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  uppercase  alphabet
																								(or)
															 When  there  are  no  lowercase  alphabets  in  the  string

2) When  does  it  return  True ?  --->  When  there  are  no  uppercase  alphabets  in  the  string
																						and
															 at  least  one  character  is  an  lowercase  alphabet

Note:
1) What  are  upper()  and  lower()  called ?  ---> Conversion  methods

2) What  are  isupper()  and  islower()  called ?  --->  Conditional  methods  becoz  they  return  True  (or)  False
'''
