'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS

Hint:  Use   sorted()  function  and   join()  method
'''
a = input("Enter  any  string  :  ")
b = sorted(a)
c = '' . join(b)
print('Sorted  string  :   ' ,  c)

sorted_name_case_insensitive = "".join(sorted(name, key=str.lower))
print(sorted_name_case_insensitive)


'''
Let  input  be  'RAJESH'
1) What  is  object  'a'  ?  --->  RAJESH

2) What  is  list  b ?  --->   ['A' , 'E' , 'H' , 'J' , 'R' , 'S']

3) What  is  object  c ?  --->  AEHJRS

4) a = 'Hyd'
    Is  a . sorted()  valid ?  --->  No   becoz  there  is  no   sorted()  method  in  str  class
'''
