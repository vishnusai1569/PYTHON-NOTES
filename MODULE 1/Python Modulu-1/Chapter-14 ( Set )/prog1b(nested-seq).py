#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})  #  {(10,20,30)}
#print({[10 , 20 , 30]})  #  Error  becoz  set can   not  have  list which  is  a  mutable
#print({{10 , 20 , 30}})   #  Error  becoz  set can   not  have  set  which  is  a  mutable
#print({{}})   #  Error  becoz  set can   not  have  dict  which  is  a  mutable




'''
1) Is  nested  set  valid ?  ---> No

2) What  is  the  issue  with  nested  set ?  ---> Set  can  not  hold  mutable  elements  such  as  list , set  and  dictionary

3) Which  elements  can  set  hold  ?  ---> Immutable  elements  such  as  int , float , str , tuple  and  so  on

4) Why  set  can  not  hold  mutable  elements ?  ---> Since  set  elements  can  not  be  modified  but  mutable  elements
														                            can  be  modified (contradiction)
'''
