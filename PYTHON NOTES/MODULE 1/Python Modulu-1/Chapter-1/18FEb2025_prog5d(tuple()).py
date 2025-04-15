# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')  #  Converts  string  to  tuple
print(a) #  ('H' , 'y' , 'd')
print(type(a)) #  <class  'tuple'>
print(len(a))  #3
b = [10 , 20 , 15 , 18]
print(tuple(b))  #  Converts  list   to  tuple  i.e.  (10,20,15,18)
print(tuple(range(5)))    #  Converts   range  object    to  tuple  i.e.  (0,1,2,3,4)
#print(tuple(25))  #  Error  becoz 25  is  not  a  sequence



'''
tuple()  function
-------------------
1) What  does  tuple(sequence)  do ?  --->  Converts  sequence  to  tuple

2) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

3) What  does  tuple(No  args)  do ?  --->  Returns  an  empty  tuple
'''
