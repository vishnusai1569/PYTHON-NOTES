 #Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c} # unpacks keys of dictionaries  a , b and c  to   form  a  set
print(d) # {10 , 20 , 15 , 18 , 14 , 25 , 19} can be any order
print(type(d)) # <class 'set'>
e = {**a , **b , **c}  #  Unpacks  dictionaries  a , b   and  to  form  a  new  dict
print(e) # {10 : 'Rama' , 20 : 'Manohar' , 15 : 'Radha' , 18 : 'Kiran' , 14 : 'Srinivas' , 25 : 'Ramesh' , 19 : 'Krishna'}
print(type(e)) # <class 'dict'>



'''
1) What  does  [*a , *b , *c]  do ?  --->  List  packing
                                                               i.e.  Packs  all  the  keys  of  dictionaries  a , b  and  c  to  form  a  list
															   [10 , 20 , 15 , 18 , 14 , 20 , 25 , 19 , 15 , 14]
															   (duplicates  are  permitted  in  the  list)

2) What  does  (*a , *b , *c)  do ?  --->  Tuple  packing
                                                                i.e.  Packs  all  the  keys  of  dictionaries  a , b  and  c  to  form  a  tuple
													            (10 , 20 , 15 , 18 , 14 , 20 , 25 , 19 , 15 , 14)
															   (duplicates  are  permitted  in  the  tuple)

3) What  does  {*a , *b , *c}  do ?  --->  Set  packing
                                                                i.e.  Packs  all  the  keys  of  dictionaries  a , b  and  c  to  form  a  set
													           {10 , 20 , 15 , 18 , 14 , 25 , 19}
								 						       (duplicates  are  not  permitted  in  the  set)

4) What  does  *a , *b , *c  do ?  --->  Tuple  packing  becoz  default  is  ()

5) Is  [**a , **b , **c]  valid ?  --->   No  becoz  list  can  not  hold   key : value  pairs
     Is  (**a , **b , **c)  valid ?  --->  No  becoz  tuple  can  not  hold  key : value  pairs
     Is  **a , **b , **c  valid ?  --->  No  becoz  tuple  can  not  hold  key : value  pairs

6) e = {**a , **b , **c}
     What  is  the  alternative  to  the  above  statement ?  ---> e = a | b | c
'''
