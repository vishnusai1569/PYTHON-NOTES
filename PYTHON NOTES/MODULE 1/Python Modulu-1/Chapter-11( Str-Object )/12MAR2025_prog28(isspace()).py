# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #   False  due  to  'A'
print('\n  \t' . isspace())  #  True
print('\n  7\t' . isspace()) #   False  due  to  '7'
print('\n' . isspace()) #  True
print('\n  $\t' . isspace()) #  False  due  to  '$'
print('\t' . isspace())   #  True
print('' . isspace())  #   False  becoz  there  are  no  white  space  chars
print(' ' . isspace()) #  True



'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  not  a  white  space
                                                               i.e.  Alphabet, digit (or)  special  character
'''
