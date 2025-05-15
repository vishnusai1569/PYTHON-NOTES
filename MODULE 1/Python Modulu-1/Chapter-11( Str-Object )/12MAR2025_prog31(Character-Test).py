'''
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  ---> Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  --->  Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  --->  Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  --->  Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->   White  space

7) What  is  the  output  if  input   is   <enter>   key ?  --->  White  space

8) Hint1:  Use  isalnum() , isalpha() , isupper() , islower() , isdigit()   and  isspace()  methods

9) Hint2:  Use  nested  if  and   elif
'''
ch = input('Enter  any  character  :  ')
if  ch . isalnum():
	print('Alpha  Numeric  Character')
	if  ch . isalpha():
		print('Alphabet  Character')
		if  ch . isupper():
			print('Upper  case  Alphabet')
		else:
			print('Lower  case  Alphabet')
	else:
		print('Digit  character')
elif  ch . isspace()  or  ch == '':
	print('White  space  character')
else:
	print('Special  character')



'''
1) What  does  input()  function  do  if  input  is  <space  bar>  ?  --->  Reads  ' '   i.e.  space

2) What  does  input()  function  do  if  input  is  <tab  key>  ?  --->  Reads  '\t'

3) What  does  input()  function  do  if  input  is  <enter  key>  ?  --->  Reads  ''  but  not  '\n'
'''
