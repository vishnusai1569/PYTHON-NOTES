# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()   #   References  a , b , c  and  d  point  to  same  object
print(sys . getrefcount(b)) #   Number  of  references  to  object   'b'  i.e.  4 + 1 = 5
print(sys . getrefcount(c1())) #  A new  object  is  created  with  0  references  i.e.  0 + 1 = 1
print(sys . getrefcount(25)) # cannot be predicted  as 25  is  an  immutable object
print(sys . getrefcount([10 , 20 , 15 , 18])) #  0 + 1 = 1
print(sys . getrefcount(10.8)) # cannot be predicted  as  10.8  is  an  immutable object
print(sys . getrefcount({10 , 20 , 15 , 18})) #  0 + 1 = 1
print(sys . getrefcount('Hyd')) # cannot be predicted as  'Hyd'  is  an  immutable object
print(sys . getrefcount({10 : 20 , 30 : 40})) #  0 + 1 = 1
print(sys . getrefcount((10 , 20 , 30 , 40))) # cannot be predicted  as  tuple  is   an  immutable object



'''
1) Which  objects  are  reusable ?  ---> All  immutable  objects  except  range  object

2) Which  objects  are  not  reusable ?  --->  All  mutable  objects  and  range  object
'''