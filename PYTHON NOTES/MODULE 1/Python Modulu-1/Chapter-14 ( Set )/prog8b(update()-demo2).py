# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set() #  Empty  set
s . update(a , b , c)  # Inserts  elements  of  sequences  a , b  and c   into   empty  set
print(s) #  {10,20,30,40,50,60,70}  in   any  order
print(len(s))  #  7
#s . add(a , b , c)  #  Error  due  to  more  than one  arg
