#  set()  function demo  program
a = set('Rama rAo')  #Converts  string  to  set
print(a) #  {'R' , 'a' , 'm' , ' ' , 'r' , 'A' , 'o'}
print(len(a)) #   7
print(set([10 , 20 , 15 , 20]))  #  Converts  list  to  set  i.e.  {10 , 20 , 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))   #  Converts  tuple  to  set  i.e.  {25 , 10.8 , 'Hyd'}
print(set(range(10 , 20 , 3)))   #  Converts   range  object  to  set  i.e.  {10 , 13 , 16 , 19}
#print(set(25))   #   Error  becoz  25  is  not  a  sequence



'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

3) What  does  set(No  args)  do ?  ---> Returns  an  empty  set
'''
