'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
a = input('Enter  any  sentence  :  ')
b = a . split()
c = ''
for  x   in   b:
	c  +=  x[ : : -1]  + ' '
print(c)



'''
a = 'Hyd'
a += 'Hyd'
What  is  the  differenece  between  the  above  two  statements ?  --->
																					a = 'Hyd'  assigns  'Hyd'  to  object  'a'
																					but  a +=  'Hyd' concatenates  'Hyd'  to  object  'a'
'''
