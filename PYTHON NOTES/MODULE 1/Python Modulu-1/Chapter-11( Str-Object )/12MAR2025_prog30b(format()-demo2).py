# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))  #    a : 25  <tab>  b : 10.8  <tab>  c :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))  #    a : 25  <tab>  b : 10.8  <tab>  c :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))  #    a :  Hyd  <tab>  b : 10.8  <tab>  c :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))  #    a :  Hyd  <tab>  b :  Hyd  <tab>  c :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))  #    a : 25  <tab>  b : 10.8  <tab>  c :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))  #    a :  Hyd  <tab>  b :  10.8  <tab>  c :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))  #    a :  25 <tab>  b :  25  <tab>  c :  25


'''
What  are  0 , 1 , 2  called ?  --->  Indexes  of  arguments  in  format()  method
'''
