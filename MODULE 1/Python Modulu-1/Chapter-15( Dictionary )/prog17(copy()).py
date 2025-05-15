# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy() # Deep clone
print(b) # {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b) # False as a and b points to different dict
print(a  ==  b) # True as a and b has same elements



'''
1) What  is  another  way  to  copy  dictionary  'a'  to  'b'  ?  --->  b = {**a}

2) What  is  the  issue  with  b = {a}  ?  --->  Set  can  not  have  mutable  element  suct  as  dictionary
'''
