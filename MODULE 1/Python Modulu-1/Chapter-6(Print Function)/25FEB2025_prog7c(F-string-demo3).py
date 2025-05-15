 #Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')  #  25  <tab>  10.8  <tab>  Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') #  a = 25  <tab>  b = 10.8  <tab> c = Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')  #  a = 25  <tab>  b = 10.8  <tab> c = 'Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}') #  25  <tab>  10.8  <tab>  Hyd  (colons  are  ignored)
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')  #  a = {a}  <tab>  b = {b}  <tab>  c = {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')  #  a = a  <tab>  b = b  <tab>  c = c
#print(F'{x =}  \t   {y =}   \t  {z =}')   #  Error  becoz  there  are  no  objects  x  ,  y  and   z



'''
How  to  obtain  quotes  for  string  output  ?   --->   print(F'{str-object=}')
'''
