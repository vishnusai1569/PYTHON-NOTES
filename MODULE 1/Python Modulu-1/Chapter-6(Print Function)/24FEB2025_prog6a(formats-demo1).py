# Formats  demo  program
a = 25.68
print('%d'  %a)  #  Converts  object  'a'  to  string   integer  i.e.  '25'
print('%s'  %a)   #  Converts  object  'a'  to  string   i.e.  '25.68'
print('%f'  %a)   #  Converts  object  'a'  to  string  float  i.e.  '25.680000'
print('%g'  %a)   #  Converts  object  'a'  to  string  float  i.e.  '25.68'
#print('%f' ,  %a)  #   Error  due  to  comma
print('a : ' ,  a)  #  a :   <space>  25.68
print('%f' ,  a)  #  %f   <space> 25.68
#print('%f'  a)     #  Error  becoz  %  is  missing  for  object  'a'
#print('a  :  '  %a)   #  Error  becoz  format   is  missing




'''
Formats
-----------
1) What  does  '%d'   %object  do ?  --->  Converts   object  to  string  integer  due  to  %d

2) What  is  '%d'  called  ?  --->  String  integer

3) What  is  the  alternative  to  '%d'  format ?  --->  '%i'  i.e.  String  integer

4) What  does  '%f'   %object  do ?  --->  Converts   object  to  string  float  with  6  digits  after  decimal  point  due  to  %f

5) What  is  '%f'  called ?  --->  String  float

6) What  is  the  alternative  to  '%f'  format ?  --->  '%g'

7) Which  is  a  better  format  between  '%f'  and  '%g' ?  --->  '%g'  becoz  unnecessary  zeroes  are  not  printed

8) How  many  digits  after  decimal  point  for  %g ?  --->  Variable  number  of  digits

9) What  does  'g'  stand  for ?  --->  general

10) What  does  '%s'   %object  do ?  --->  Converts   object  to  string  due  to  %s

11) What  is  %s  called ? ---> String

12) What  is  %  in  '%s'  called  ?  --->  Format  specifier

13) What  are  the  two  ways  to  convert  object  to  string ?  --->  str(object)  and  '%s'   %object
'''
