'''
Write  a  program  to  validate  vehicle  registration  number

Rules:
1) First  2  characters  shoulde  be  TS , ts , Ts  or  tS

2) There  are  29  circles  i.e.  01 , 02 , 03 , ......29

3) Next  two  characters  should  be  alphabets

4) Last  four  characters  should  be  digits

5) Which  of  the  following  is  valid  ?
     a) TS30AB1234 ---> Invalid  becoz  circle  30  does  not  exist
     b) AP15CD1234  ---> Invalid  becoz  first  2  characters  can  not  be  AP
     c) Ts15E1234 --->  Invalid  due  to  single  character  'E'
    d) tS15FG123 --->  Invalid  due  to  3-digit  number  123
    e) ts9KP1234 --->	Invalid  due  to  single  digit  9
    f) tS10LW1234  ---> Valid
    g) 15XY1234  --->	Invalid  becoz  TS   is  missing
    h) Ts00PQ1234  ---> Invalid  becoz  circle  00  does  not  exist
    i)  TS20RS1234 ---> 	Valid
    j) Ts25TR1234 --->	Valid

6) What  is  the  regular  expression  for  the  above  rules ?  --->  TS(0[1-9]|[12][0-9])[A-Z]{2}[0-9]{4}

7) [TS](0[1-9]|[12][0-9])[A-Z]{2}[0-9]{4}
   What  is  the  issue  when  TS  is  in  [] ? --->  Number  may  start  with  T  (or)  S  but  not  TS

8) (TS)(0[1-9]|[12][0-9])[A-Z]{2}[0-9]{4}
    Can  TS  be  in  () ?  --->  Yes  becoz  ()  are  optional  as  it  is  single  element  TS

9) TS[01-29][A-Z]{2}[0-9]{4}
    What  is  the  issue  with  the  above  regular  expression  ?  --->  0 , 1 , 2 (or) 9  but  not  01  to  29
    Is  TS25AB1234  valid  for  the   above  regular  expression ?  ---> Invalid  due  to  2-digit  number  25
    Is  TS2AB1234  valid  for  the   above  regular  expression ?  --->  Valid  due  to  2
    Is  TS5AB1234  valid  for  the   above  regular  expression ?  --->  Invalid  Valid  due  to  5
'''
import re
vehiclenumber  =  input('Enter  Vehicle registration number : ')
m  =  re . fullmatch('TS(0[1-9]|[12][0-9])[A-Z]{2}[0-9]{4}' , vehiclenumber , re . IGNORECASE)
if   m:
	print('Valid  number')
else:
	print('Invalid  number')