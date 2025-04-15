# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #  {'Hyd' , 25 , True , 10.8}  in   any  order
print(a . pop()) # Removes  first  element  Hyd  from set and returns  Hyd
print(a . pop()) # Removes  first  element 25   from set and returns  25
print(a . pop())  # Removes  first  element  True   from set and returnsTrue
print(a . pop()) # Removes  first  element  10.8  from set and returns   10.8
#print(a . pop()) # error as there are no elements to delete
print(a) #  set()
b = {10 , 20 , 30 , 40}
#print(b . pop(2)) #  Error  becoz  set  is not indexed




'''
pop()  method
----------------
1) What  does  pop(No  args)  method  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

2) What  does  emptyset . pop()  do ?  ---> Throws  error

3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

4) How  many  arguments  can  pop()  method  take  ?  ---> Zero
'''
