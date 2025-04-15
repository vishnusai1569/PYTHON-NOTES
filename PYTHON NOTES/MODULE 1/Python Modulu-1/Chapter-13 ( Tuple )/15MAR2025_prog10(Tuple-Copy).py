# How  to  copy  tuple ?   (Home  work)
a = (10 , 20 , 15 , 18)
print(id(a)) #   Address  of  tuple  (may  be   1000)
#b = a . copy()  #  Error becoz  there  is  no  copy()  method  in  tuple
b = tuple(list(a))  # How  to  copy  elements  of   tuple  'a'  to  tuple  'b'
print(b) #  (10,20,15,18)
print(id(b)) #  Different  address
print(type(b))  #   <class  'tuple'>
print(a  is   b)#   False  becoz  'a'  and  'b'  point  to  different  tuples
print(a   ==   b) #  True  becoz  elements  of   tuples  'a'  and  'b' are  same


'''
Which  of  the  following  is  shallow  clone(Assume  that  'a'  is  tuple) ?
1) b = a[:]   --->  Shallow  clone
                         i.e.  Ref  'b'  points  to  same  tuple  where  'a'  points

2) b = tuple(a) --->  Shallow  clone  becoz  tuple  'a'  is  converted  to  same  tuple

3) b = a  ---> Shallow  clone

4) b = tuple(list(a))  --->  Deep  clone
                                       i.e.  Elements  of  tuple  'a'  are  copied  to  tuple  'b'

5) b = (*a,)  ---> Deep  clone
                          i.e.  Elements  of  tuple  'a'  are  copied  to  tuple  'b'

6) b = (*a)  --->  Error  becoz  comma  is  missing

7) b = a . copy()  ---> Error  becoz  there  is  no  copy()  method  in  tuple
'''
