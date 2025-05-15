# Find  outputs (Home  work)
a = 'RAMA'
b = reversed(a)
print(type(b)) # <class 'reversed'>
print(b) #  __str__()  returns type and address of the object
print(id(b)) # address   of  reversed  object  'b'
print(*b) #  Stores  all  the  characters  of   the  string  in   reversed  object  in  reverse  order   and  unpacks  the  object b  i.e. A <space> M  <space>  A  <space>  R
#print(b[0]) #  Error :  iterator is not indexed
#print(b[1 : 3]) # Error :   iterator  can  not  be  sliced   as  there  are  no  indexes
#print(b * 2) # Error :  iterator  can  not  be  repeated
#print(len(b)) #  Error :   'b'  is  not  a  sequence