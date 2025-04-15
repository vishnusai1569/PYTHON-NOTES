'''# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
'''

a=[25,10.8,'hyd',True]
for i in range(len(a)):
    print(i)

print("each  element  and  the  corresponding  index  with  index  based  for  loop")


for i in range(len(a)):
    print(i,a[i])

print("each  element  and  the  corresponding  index  with  for  ...  each  loop")


for i in a:
    print(a.index(i),i)




