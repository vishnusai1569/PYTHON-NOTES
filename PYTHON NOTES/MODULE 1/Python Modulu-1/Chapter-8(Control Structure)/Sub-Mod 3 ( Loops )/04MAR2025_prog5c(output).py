# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
for  i  in  range(len(a)):  #  How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
	print(i , a[i] , sep = '...')  #  0 ... 25  <next  line>  1  ...  10.8 <next  line>  2  ...  Hyd  <next  line> 3  ... True  <next  line>
print('For each loop')
for  x  in   a:  #  How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
	print(a . index(x) , x , sep = ' : ')   #  0 :  25  <next  line>  1  : 10.8 <next  line>  2  : Hyd  <next  line> 3  : True  <next  line>
