'''
#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop
'''
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
for i in range(2,len(a)-2):
    print(a[i])
print()