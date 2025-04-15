#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]   #  List  due  to  []
print(a)  #  [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]  
print(*a)  # Unpacks  list  into  elements  i.e.  25  <space>  10.8  <space>  Hyd  <space>  True <space> 3+4j  <space>  None <space>  Hyd  <space>  25
print(type(a))#  <class  'list'>
print(id(a)) #  Address  of   list 
print(len(a))  #  8
a[2] = 'Sec'  #  Element  at index  2  is  modified  to  'Sec'
print(a) #  [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]   
print(a[2 : 5])  #  List  from  indexes  2  to  4  in  steps  of   1  i.e.  ['Sec' , True ,  3+4j]
