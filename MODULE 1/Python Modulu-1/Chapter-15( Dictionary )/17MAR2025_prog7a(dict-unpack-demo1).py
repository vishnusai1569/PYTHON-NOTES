#  *   and  **  operators  demo  program
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {*a}  #  Unpacks  all  the  keys  of  dict  'a'  to  form  a  set
print(b)  #   {10,20,15,18}  in  any order
print(type(b)) #  <class  'set'>
c = {**a}  #  Unpacks  all  the  key : value  pairs  of  dict  'a'  to  form  a   new dictionary  with  same  key : value  pairs
print(c)#   {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(type(c))  #  <class  'dict'>
print(a   is   c) #   False  becoz   'a'  and  'c'  point  to  different  dictionaries
print(a  ==   c) #   True  becoz dictionaries  'a'  and  'c'  have  same  key : value pairs


'''
1) What  does  {*dict}  do  ?  --->   Unpacks  dictionary  to  form  a  set  of  keys  (due  to  { })
                                                       i.e.  {k1 , k2 , k3 ... }
    What  does  [*dict]  do  ?  --->  Unpacks  dictionary  to  form  a  list  of  keys  (due  to  [] )
    	                                              i.e.  [k1 , k2 , k3 ...]
    What  does  (*dict)  do ?  ---> 	Throws  error  becoz  ,  is  missing  as  tuple  has  got  single  element
    What  does  (*dict,)  do ?  --->  Unpacks  dictionary  to  form  a  tuple  of  keys  (due  to  comma)
  	                                                  i.e.  (k1 , k2 , k3 ...)
    What  does  *dict,   do ?  --->  Unpacks  dictionary  to  form  a  tuple  of  keys  (due  to  comma)

2) What  does  {**dict}  do  ?  --->  Unpacks  dictionary  to  form  a  new  dictionary  with  same  key : value  pairs
     Is  [**dict]  valid ?  --->   No  becoz  list  can  not  hold  key : value  pairs
     Is  (**dict)  valid ?  --->  No  becoz  ,  is  missing  as  tuple  has  got  single  element
     Is  (**dict,)  valid ?  --->	 No  becoz  tuple  can  not  hold  key : value  pairs
     Is  **dict  valid ?  --->	 No  becoz  ,  is  missing  as  tuple  has  got  single  element

3) Are  **list , **tuple  and  **set  valid ?  ---> No  becoz  they  don't  contain  key : value  pairs  and  hence  **  is  not  permitted

4) What  is  the  difference  between  dict . keys()  and  [*dict] ?  --->
			 dict . keys()   --->  Keys  are  stored  in  list  and  list  in  dict_keys  object(nested  objects)
			 [*dict]  --->  Keys  are  stored  in  list (single  object)

5) What  is  the  difference  between  dict . items()  and  {**dict} ?  --->
					 dict . items()   --->  Keys  and  values   are  stored  in  tuples ,  each  tuple  is in  list  and
												    list  in  dict_items  object(nested  objects)
					 {**dict}  --->  Keys  and  values   are  stored  in   another  dictionary

6) Are  {**dict}  and  dict  same  ?  --->  No  becoz  {**dict}  is  a  new  dictionary  but  dict  is  original  dictionary
'''
