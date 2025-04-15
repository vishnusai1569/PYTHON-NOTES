# Find  outputs (Home  work)
a = 25.7  #   Ref 'a'  points  float  object  25.7
print(id(a)) #  Address  of   object  25.7  (1000)
print(a)  #  25.7
a = 35.6 #   Ref  'a'  is  modified  to  another  object  35.6
print(id(a)) #  Address  of   object  35.6  (2000)
print(a)  #  35.6
b = True #   Ref 'b'  points  object  True
print(id(b))  #  Address  of   object   True  (3000)
b = False  #   Ref  'b'  is  modified  to  another  object   False
print(id(b))    #  Address  of   object   False  (4000)
c = None   #   Ref  'c'  points  object  None
print(id(c))  #  Address  of  object  None  (5000)
c = None  #  Nothing  is  modified
print(id(c)) #   Same  address  (5000)
