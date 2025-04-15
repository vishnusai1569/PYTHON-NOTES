# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)  # {100,110,120,130,140,150}  in  any  order
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)  #  {10,20,15,18,50,12}  in  any  order
e = set('Rama  rAo')
print(e)  #  {'R' , 'a', 'm' , ' ' , 'r' , 'A' , 'o'}  in any  order
#print(set(25)) #   Error  becoz  25 is  not  a  sequence
print(set())  # Returns  an  empty set



'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  --->  Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''
