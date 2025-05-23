'''
Write  a  regular  expression  to  represent  a  10-digit  mobile  number

Rules:
1) It  should  be  a  10-digit  number

2) First  digit  can  be  7 , 8  or  9

3) Number  may  start  with  0  (or)  +91

4) Which  of  the  following  are  valid ?
     a) 6948250500  ---> Invalid  becoz  first  character  '6'  is  not  between  '7'  and  '9'
     b) 994825050 --->  Invalid  becoz  length  of  the  string  is  not  10
     c) 9948-250500  --->  Invalid  due  to  '-'
     d) 9948250500  --->  Valid
     e) 09948250500  --->  Valid  becoz  number  may  start  with  '0'
     f) +919948250500 ---> Valid  becoz  number  may  start  with  +91
     g) 919948250500  ---> Inavlid  becoz  length  of  the   string  is  not  10

5) What  is  the  regular  expression  for  the  above  rules ?  --->  (0 | [+]91)?[789][0-9]{9}

6) Which  function  should  be  used ?  --->  fullmatch()  function
'''
import re
mobilenumber  =  input('Enter mobile number : ')
m  =  re . fullmatch('(0|[+]91)?[789][0-9]{9}'  ,  mobilenumber)
if  m:
	print('Valid mobile number')
else:
	print('Invalid mobile number')


'''
1) (0|[+]91)?[789][0-9]{9}
    What  is  the  issue  when  ?  is  omitted  from  the  above  regular  expression ? --->
											Number  must  start  with  '0'  (or)  '+91'  which  is  aganist  to  rule  3

2) (0|[+]91)?[789][0-9]{9}
    What  is  the  issue  when  +  is  not  in  [] ? --->  Error  becoz  character  is  expected  before  wild  character  '+'

3) What  is  the  difference  between  +  and  [+] ?  --->  [+]  indicates  character  +   and
                                                                                          +  indicates  wild  character  i.e.  repetion  operator

4) What  does  'a+'  mean  ?  --->  At  least  one  'a'

5) Hence  '+'  should  be  in  []

6) What  is  '|'  operator  called  ?  --->  Bitwise  or  operator

7) What  does  (0|[+]91)  indicate ? --->  Either  0  or  +91

8) What  does  [0|[+]91]  indicate ? --->  Any  character  like  0 , | , [ , + , ] , 9 (or) 1
'''