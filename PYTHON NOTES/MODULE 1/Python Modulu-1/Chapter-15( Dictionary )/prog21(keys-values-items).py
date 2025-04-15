#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys() #  Unpacks  dict_keys  object into  3  objects
print(x) # 10
print(y) # 20
print(z) # 30
print()
x , y , z = a . values()  #  Unpacks  dict_values  object into  3  objects
print(x) # Rama
print(y) # Sita
print(z) # Rajesh
print()
x , y ,  z = a . items()  #  Unpacks  dict_items  object into  3   tuples
print(x) # (10 , Rama)
print(y) # (20 , Sita)
print(z) # (15 , Rajesh)
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items() #    Unpacks  dict_items  object into  3   tuple  and  each  tuple  is  further  unpacked  into  2  elements
print(rno1 , sname1)  # 10  <space> Rama
print(rno2 , sname2) # 20  <space>  Sita
print(rno3 , sname3)  # 15  <space> Rajesh


'''
What  is  the  alternative  to  x , y , z = a . keys()  ?  --->  x , y , z = a
'''
