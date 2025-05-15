#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b) # error  becoz  dictionaries  cannot be concatenated with +
c = {**a , **b}  # Concatenates  dictionaries  'a'  and  'b'  to  form   a  new  dictionary
print(c) # {10 : 60 , 30 : 50}
d = a | b   # Concatenates  dictionaries  'a'  and  'b'  to  form   a  new  dictionary
print(d)   # {10 : 60 , 30 : 50}



'''
1) What  are  the  two  ways  to  concatenate  dictionaries ?  --->  dict1 | dict2 | dict3 ......
																															(or)
																										  {**dict1 , **dict2 , **dict3 , ....}

2) How  to  concatenate  lists ?  ---> list1 + list2 + list3 +  ....
    How  to  concatenate  tuples ?  --->  tuple1 + tuple2 + tuple3 + ....
    How  to  concatenate  strings ?  ---> str1 + str2 + str3 + .....
    How  to  concatenate  sets ?  --->  set1 | set2 | set3 | .....
'''
