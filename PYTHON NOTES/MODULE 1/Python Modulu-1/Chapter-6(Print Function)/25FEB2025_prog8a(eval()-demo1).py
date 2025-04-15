# eval()  function  demo  program
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False'))  #  Converts  'False'  to    False
print(eval('3+4j'))  #  Converts  '3+4j'  to   3+4j
#print(eval('Hyd'))  #   Error  becoz  'Hyd'  is  converted  to  object  Hyd  which  does  not  exist
print(eval("    'Hyd'   "))  #  Converts  "  'Hyd'   "    to   'Hyd'
print(eval('3 + 4 * 5'))  #  Converts  '3 + 4 * 5'  to   3 + 4 * 5 = 23
print(eval('[10 , 20 , 15 , 18]'))  #  Converts  '[10 , 20 , 15 , 18]'  to   [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}'))   #  Converts   '{10,20,15,18,20,12,18}'  to  {10,20,15,18,12}
print(eval('(10 , 20 , 30)'))  #  Converts  '(10,20,30)'  to  (10,20,30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))  #  Converts  "{10 : 'Hyd' , 10 : 'Sec'}"   to   {10 : 'Sec'}
#print(eval(4 + 5))  #  Error  becoz  4 + 5  is  not  a  string


'''
eval()  function
------------------
1) What  does  eval()  function  do ?  --->  Converts  string  to  appropriate  object

2) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer
    What  does  float(x)  do  ?  ---> Converts   object  'x'   to  float
    What  does  complex(x)  do  ?  ---> Converts   object  'x'  to  complex  number
    What  does  bool(x)  do  ?  ---> Converts   object  x'  to  boolean

3) What  is  the  advantage  of  eval()  function ?  --->
													It  can  be  used  as  an  alternative  to  int() , float() ,  complex() , bool()  and  so  on
'''
