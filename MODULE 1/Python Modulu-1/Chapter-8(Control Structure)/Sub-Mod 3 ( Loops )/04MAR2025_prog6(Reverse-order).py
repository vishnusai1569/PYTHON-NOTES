#  How  to  print  list  elements  in  reverse  order   without  slice
a = eval(input('Enter  list  of  elements : '))   #  [10 , 20 , 15 , 18 , 10 , 18]
print('Indexed for loop')
for  i   in   range(1 , len(a) + 1):  # How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
		print(a[-i])
#  How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable)  --->  Not  possible


# for ... each  loop  can  iterate  sequence  from  left  to  right  but  not  from right  to  left  (i.e.  reverse  order)
