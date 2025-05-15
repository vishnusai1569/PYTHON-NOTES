# sorted()  function  demo  program
a = 'RAJESH'
b = sorted(a)  #  Returns  a  list  of  sorted  characters
print(type(b))  #  <class  'list'>
print(b)  #  ['A' , 'E' , 'H' , 'J' , 'R' , 'S']
c = sorted(a , reverse = True)  #  Returns  a  list  of  sorted  characters  in  descending  order
print(c)  #  ['S' , 'R' , 'J' , 'H' , 'E' , 'A']
print(a)  #  RAJESH


'''
sorted()  function
----------------------
1) What  does  sorted()  function  do ?  --->  Returns  a  list  of  sorted  characters  in  alphabetical  order

2) What  is  the  argument  of  sorted()  function ?  --->  Any  sequence

3) What  does  sorted()  function  return ?  --->  List  of  sorted  characters

4) In  other  words,  sorted()  function  deos  not  return  sorted  string

5) list = sorted(sequence)
    Is  sequence  modified  after  execution  of  the  function ?  --->  No  and  results  are  stored  in  list
'''
