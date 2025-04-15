#  Find  outputs
a = 25  #  Ref  'a'  points  to  object  25
print(id(a)) #  Address  of  object   25 (may  be  1000)
a = 35  #  Ref  'a'  is modified  to  another  object  35
print(id(a))  #  Address  of  object   35 (may  be  2000)



'''
1) a = 25
    a = 35
    Why  is  25  not  replaced  with  35  when  a = 35  is  executed ? ---> Since  int  object  is  immutable

2) What  is  modified  when  a  = 35   is  executed  ?  --->  Reference  but  not  object

3) How  many  objects  are  in  the  program ?  ---> Two  i.e.   25  and   35
'''
