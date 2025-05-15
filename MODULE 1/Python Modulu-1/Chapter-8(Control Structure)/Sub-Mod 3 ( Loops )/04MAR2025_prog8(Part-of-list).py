#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
for  i  in  range(2 , 5):  # How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
	print(a[i]) #   Hyd  <next line>  True <next  line>  3+4j  <next  line>
#  How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  index()  method  and  any  other  variable  --->  Not  possible


# for ... each  loop  can  iterate  whole  sequence  but  not  a  part  of  the  sequence
