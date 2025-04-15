'''
#How  to  print  list  elements  in  reverse  order   without  slice
a = eval(input('Enter  list  of  elements : '))
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable)
[10,20,30,40]
'''

a =eval(input('Enter  list  of  elements : '))
for i in range(1,len(a)+1):
    print(a[-i])
print("\n")
#not possible for for each loop


