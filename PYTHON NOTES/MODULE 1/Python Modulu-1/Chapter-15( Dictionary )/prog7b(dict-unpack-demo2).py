#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a} # unpacks dict  'a'  to  another  dict with same key value pairs
print(b) # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b) # False as a and b points to different  dictionaries
print(a  ==  b) # True as a and b has same  key : value  pairs
c = a  #  'c'  points to  dict  'a'
print(a  is   c) # True as a and c points to same dictionaries
print(a  ==  c) # True as a and c has same  key : value  pairs



'''
1) What  is  b = {**a}  called ?  --->  Deep  clone

2) What  is  b = a  called ?  ---> Shallow  clone

3) What  is  the  alternative  to  b = {**a}  ?  --->  b = a . copy()
'''
