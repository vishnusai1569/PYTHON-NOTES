# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl  #  Unpacks   tuple  into 3  objects
print(a) #  25
print(b)#  10.8
print(c) #  ['Hyd', True]
print(type(c))#   <class  'list'>


'''
What  is  obtained  when  tuple  is  unpacked  with  *  operator ?  --->  List
'''
