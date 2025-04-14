# Find  outputs
a  =  lambda  :  print('Hyd'); print('Sec')  ;  print('Cyb')
a()

'''
Sec
Cyb
Hyd
'''


'''
1) How  many  statements  can  be  in  a  lambda  function ?  ---> Single  statement.

2) What  happens  when  there  are  multiple  statements  in  lambda  function ?  --->
																First  statement  is  treated  as  a  part  of   lambda  function  and
																rest  are  outside  the  function

3) a = lambda  :  print('Hyd') ; print('Sec') ; print('Cyb')
    How  is  the  above  statement  interpreted ? --->	a = lambda  :  print('Hyd');
																				    print('Sec'); ---> They  are  outside lambda  function
																				    print('Cyb')

4) stmt1 ;  stmt2 ; stmt3 ;
     Is   ;  mandatory  between  the  statements ?  --->  Yes  becoz  they  are  in the  same  line

5) stmt1;
    stmt2;
    stmt3;
    Is   ;  mandatory  ?  --->  No  becoz  each  statement  is  in  a  different  line
'''
