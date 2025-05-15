#  join()   method  demo  program
a = ['15' , 'Aug' , '1947']
print('-' . join(a))  #  All  the  strings  of  list  'a'  are  joined  with  '-'  to  form  a  string  i.e.  '15-Aug-1947'
print('' . join(a))    #  15Aug1947
print(' ' . join(a))  #  15<space>Aug<space>1947
#print(a . join(':'))  #  Error  becoz  there  is  no  join()  method  in  list  class  as  'a'  is  list  class  object



'''
join()  method
-----------------
1) What  does  join()  method  do ?  --->  Joins  a  sequence  of  strings  with  delimeter  to  form  a  new  string

2) What   are  input  and  output  of  join()  method ?  --->  Input  is  sequence  of  strings  and  output  is  string

3) What  is  the  argument  of  join()  method ?  --->  Sequence  of  strings

*4) In  other  words,  join()  method  converts  sequence  of  strings  to  a  string
       Eg:  Converts  list / tuple / set  to  a   string

5) a = (15 , 'Aug' , 1947)
    Is  '/' . join(a)  valid ?  ---> No  becoz  15  and  1947  are  not  strings  in  tuple  'a'

6) What  is  the  difference  between  split()  and  join()  methods ?  --->
														split()  method  converts  string  to  a   list  of  strings but
														join()  method  converts  a  sequence  of  strings  to  a  string

7) In  other  words,  split()  and  join()  are  quite  opposite  methods
'''
