# Find  outputs  (Home  work)
a = b = c = 25   #  References  a, b  and  c  point  to  same  object  25
print(a , b , c)  #  25  <space>  25  <space>  25
del   a   # Deletes  ref  'a'  but  not  object
print(b , c) #  25 <space>  25
#print(a)  #   Error becoz  ref 'a'  does  not  exist
del   b  # Deletes  ref  'b'  but  not  object
print(c)  #   25
#print(b)  #   Error becoz  ref 'b'  does  not  exist
del   c   # Deletes   both  ref  'c'   and  object
#print(c)  #   Error becoz  ref 'c'  does  not  exist
