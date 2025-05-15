# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #   {'Hyd' , 25 , True , 10.8}  in  any  order
print(a . pop())  #  Hyd
print(a . pop())  # 25
print(a)
print(a . pop()) #  True
print(a . pop()) #  10.8
#print(a . pop()) #  Error  due  to  empty  set
print(a)  #  set()
b = {10 , 20 , 30 , 40}
#print(b . pop(2)) #  Error  due  to  argument  2  (index  is  not  supported)



'''
pop()  method
----------------
1) What  does  pop(No  args)  method  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

2) What  does  emptyset . pop()  do ?  ---> Throws  error

3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

4) How  many  arguments  can  pop()  method  take  ?  ---> Zero
'''
