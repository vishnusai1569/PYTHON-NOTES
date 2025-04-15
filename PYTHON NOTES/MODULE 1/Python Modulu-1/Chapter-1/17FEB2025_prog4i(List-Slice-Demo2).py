#  Find  outputs  (Home  work)
#        0      1         2        3          4         5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]  #  x , y = list[3 : 5 : 1]  ---> List  from  indexes  3  to  4  in  steps  of   1  i.e.  ['Hyd' , True]
print('x : ' , x)  # x :  Hyd
print('y : ' , y)  # y : True
for  x  in  list[2:7]:  #   List  from  indexes  2  to  6  in  steps  of  1  i.e.  [3+4j , 'Hyd' , True , None , 10.8]
	print(x)  #   3+4j  <next  line>  Hyd   <next  line>   True   <next  line> None   <next  line>  10.8   <next  line>


'''
The  above  for  loop  iterates  a  part  of  the  list  due  to  slice
'''
