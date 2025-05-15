# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)   #  {25, 10.8, 'Hyd', True}  in  any  order
print(id(a)) #  Address  of   set  (1000)
a . add(tpl)  #  Inserts  tuple  into  set  'a'  any  where  in  the  queue
a . add('Sec')  #  Inserts  'Sec'  into  set  'a'  any  where  in  the  queue
print(a) #  {True, 'Sec', 10.8, 'Hyd', (10, 20, 30), 25}  in  any  order
print(id(a)) # Same  address
print(len(a))  #  6
#a . add([100 , 200 , 300])  # Error  due  to  mutable  argument  such  as  list
#a . add(set())  # Error  due  to  mutable  argument  such as  set
#a . add({ })  # Error  due  to  mutable  argument  such as  dict
