#  How  to  print  list  in  different  ways  (Home  work)
a = [25 , 10.8 , 'Hyd' , True]        
print('List  with   print   function')
print(a)  #  [25 , 10.8 , 'Hyd' , True]
print('Elements  of  list  without  using  indexes')
for  x  in   a:  #  How  to  print  each  element  of  list  using  for  loop  without  using  indexes
	print(x)  #  25  <next  line>  10.8   <next  line>  Hyd   <next  line>  True   <next  line>
print('Elements  of  list  using indexes')
for   i  in  range(len(a)):  #   prints  a[i]  where  'i'  varies  from  0  to  len - 1 
		print(a[i])   #  25  <next  line>  10.8   <next  line>  Hyd   <next  line>  True   <next  line>
print('Elements  of  list  in  reverse  order  without  slice')
for  i  in  range(1 , len(a) + 1):  #  prints  a[-i]  where  'i'  varies  from  1  to  len 
		print(a[-i])  #   True  <next  line>   Hyd  <next  line>  10.8  <next  line>   25  <next  line>
print('Reverse  List  with  slice')
print(a[::-1])  #  a[-1 : -5 : -1]  ---> List  from  indexes  -1  to   -4  in  steps  of   -1   i.e.  [True , 'Hyd' , 10.8 , 25]


'''
1)  for   x  in   a:
                print(x)
     Iteration         x
  ---------------------------
           1                25
           2               10.8
           3               Hyd
           4               True

2) for  i  in   range(len(a)):
                print(a[i])
        i        a[i]
     -------------------
        0       25
        1       10.8
        2      Hyd
        3      True
	What  is  the  difference  between  a[i]  and  'i' ?  ---> 
																		a[i]  is  each  element  of  list  and  'i'  is  index  of  each  element  of  list

3)  for  i   in   range(1 , len(a) + 1):
                print(a[-i])
        i          a[-i]
    ---------------------
        1           a[-1]   --->  True
        2           a[-2]   --->  Hyd
        3           a[-3]   --->  10.8
        4           a[-4]   --->  25

4) What  is  the  result  of  string[::-1] ?  --->  Reverse  string
    What  is  the  result  of  list[::-1] ?  --->  Reverse   list
'''
