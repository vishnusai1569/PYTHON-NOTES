#  Gift
# add()  and  remove()  methods  (Home  work)
a = set()  #   Empty  set
a . add(25) #  Inserts  25 into  empty  set
a . add(10.8)  #   Inserts  10.8  any  where  in the  set
a . add('Hyd')   #   Inserts   'Hyd'   any  where  in the  set
a . add(True)   #   Inserts  True  any  where  in the  set
a . add(None)   #   Inserts  None   any  where  in the  set
a . add('Hyd')   #  Ignored  becoz set  already  contains  'Hyd'
a . add(1)  #  Ignored  becoz set  already  contains  True
print(a)  # {25 , 10.8 , 'Hyd' , True , None}  in  any  order
a . remove(25)    #  Removes  25  from  set  'a'
print(a)   # {10.8 , 'Hyd' , True , None}  in   same  order  (same  as  line  11)
#a . append(100) #   Error  becoz  there  is  no  append()  method in  set




'''
1) Which  method  is  used  to  append  an  element  to  list  ?  --->  append()  method

2) Which  method  is  used  to  insert  an  element  into  set  ?  --->  add()  method

3) Which  method  is  used  to  remove  an  element  from  list  and  set  ?  ---> remove()  method

4) a = {25 , 10.8 , 'Hyd' , True}
     print(a)
     print(a)
     print(a)
     Is  set  printed  in  the  same  order  all  the  three  times  ?  --->  Yes  becoz  it  is  the  same  set

5) a = {25 , 10.8 , 'Hyd' , True}
     print(a)  --->  {10.8 , True , 'Hyd' , 25}
     Is  set  printed  in  the  same  order  every  time  program  is  executed ?  ---> Not  guranteed
'''
