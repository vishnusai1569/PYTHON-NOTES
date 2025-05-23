'''
Write  a  regular  expression  to  represent  a  language  identifier

Rules:
1) Valid  characters  are  a-z , A-Z , 0-9  and  #

2) First  character  should  be  a  lower  case  alphabet  between  a  and  k

3) Second  character  should  be  a  digit  divisible  by  3

4) Identifier  should  have  atleast  two  characters

5) Which  of  the  following  are  valid ?
     a) m9A8  --->  Invalid  becoz  first  character  'm'  is  not  between  'a'  and  'k'
     b) c7  ---> Invalid  becoz  2nd  character  '7'  is  not  divisible  by  3
     c) b0aG$  --->  Invalid  due  to  special  character  '$'
     d) a  --->  Invalid   becoz  string  length  is  <  2
     e) D6ag#7  --->  Invalid  becoz  first  character  is  upper  case  alphabet
					            i.e.  'D'  is  not  between  'a'  and  'k'
     f) d6aM#7  ---> Valid
     g) j9  --->  Valid

6) What  is  the  regular  expression  for  the  above  rules ?  --->  [a-k][0369][A-Za-z0-9#]*

7) Which  function  should  be  used  ?  --->  fullmatch()  function
'''
import re
identifier = input('Enter  any  Identifier : ')
m  = re . fullmatch('[a-k][0369][A-Za-z0-9#]*' ,  identifier)
if   m:
	print('Valid')
else:
	print('Invalid')


'''
1) Let  the  regular  expression  be  [a-k][0369][A-Za-z0-9#]
    Can  length  of  identifier  be  >  3  for  the  above  regular  expression ?  --->  No  becoz  *  is  missing
    Can  length  of  identifier  be  <  3 ?  --->   No  becoz  *  and  ?   are  missing
    Can  length  of  identifier  be  3 ?  --->  Yes
    In  other  words,  identifier  should  be  3-character  string  which  is  aganist  to  rule  4

2) Let  the  regular  expression  be  [a-k][0369][A-Za-z0-9#]+
    Can  length  of  identifier  be   2  for  the  above  regular  expression ?  --->  No  due  to  +
    In  other  words,  identifier  should  be  at  least  3-character  string  which  is  aganist  to  rule  4

3) Let  the  regular  expression  be  [a-k][0369]*[A-Za-z0-9#]*
    Can  length  of  identifier  be  2  for  the  above  regular  expression ?  --->  No  due  to  *  after  [0369]
    In  other  words,  identifier  can  be  single  character  string  which  is  aganist  to  rule  4
'''