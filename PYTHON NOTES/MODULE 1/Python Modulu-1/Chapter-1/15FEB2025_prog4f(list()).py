# list()  function  demo  program
a = list('Hyd')  #  Converts  string  to  list
print(a)      #  ['H' , 'y' , 'd']
print(type(a))  #  <class  'list'>
print(len(a))   # 3
b = (10 , 20 , 15 , 18)  # Tuple  due  to  ()
print(list(b))  #  Converts   tuple  to  list   --->  [10,20,15,18] 
print(list(range(5)))  #  Converts   range   object   to  list   --->  [0,1,2,3,4]
#print(list(25))  # Error  becoz  25  is  not  a  sequence


'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

3) What  does  list(No  args)  do ?  --->  Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
'''
