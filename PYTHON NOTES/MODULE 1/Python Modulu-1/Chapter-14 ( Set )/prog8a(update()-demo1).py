# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()  #  empty  set
s . update(tpl)  #  inserts  elements  of  tuple  into  empty  set
print(len(s)) #   4
print(s) #   {10,20,15,18}  in  any order
#s . update(25) #  Error  due  to  non-sequence  arg



'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  ---> Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
											                        (Like  extend()  method  of  list  class)

2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

3) How  many  arguments  can  update()  method  take ?  --->  One  (or)  more  than   one
'''
