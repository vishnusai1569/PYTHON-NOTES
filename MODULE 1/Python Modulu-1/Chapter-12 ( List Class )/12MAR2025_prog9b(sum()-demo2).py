#  Find  outputs
a = [[10 , 20 , 15 , 1850,60,70]]
#print(sum(a))  #   0 + [10,20,15,18] throws  error
print(sum(a[0]))  #  How  to  determine  sum  of  inner  list  elements  --->  sum([10,20,15,18])  --->  63
print(sum(*a))  #  How  to  determine  sum  of  inner  list  elements  in  another  way  --->  sum([10,20,15,18])  --->  63



'''
1) a = [[10,20,15,18]]
    What  is  a[0] ?  ---> Inner  list  [10,20,15,18]

2) What  does  *a  do ?  ---> Unpacks  outer  list  to  obtain  inner  list
'''
