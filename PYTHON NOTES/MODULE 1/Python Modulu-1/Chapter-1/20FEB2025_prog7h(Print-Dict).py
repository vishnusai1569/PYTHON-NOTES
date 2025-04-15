# Gift
# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
print(a)  #  How  to  print  dictionary  --->  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Keys  of  dictionary')
for  x    in  a . keys():   #  'x' is  each  element  of  the  list  in  dict_keys  object
		print(x)  # 10  <next  line>  20  <next  line>  15 <next  line>  18 <next  line>
print('Values  of  dictionary')
for   x  in  a . values():   #  'x' is  each  element  of  the  list  in  dict_values  object
		print(x)  #  Ramesh  <next  line>  Kiran   <next  line>    Amar  <next  line>   Sita  <next  line>
print('All  the  tuples  of  dict_items   object')
for   x   in  a .  items():   #  'x' is  each   tuple  of  the  list  in  dict_items  object
		print(x)  #  (10 , 'Ramesh')  <next  line>  (20 , 'Kiran')  <next  line>  (15 ,  'Amar')  <next  line> (18 , 'Sita')  <next  line>
print('Elements  of  each   tuple')
for   x , y   in  a .  items():   #  'x'   and  'y'  are  elements  of  each   tuple  of  the  list   of   dict_items  object
		print(x , y , sep = '...')  #  10  ...  Ramesh  <next  line>   20  ...  Kiran   <next  line>   15  ...  Amar   <next  line>  18  ... Sita  <next  line>
print('Keys  and  values  of  dictionary')
for   x   in  a . keys():   #  'x' is  each  element  of  the  list  in  dict_keys  object
		print(x , a[x] , sep =  ' : ')    #  10 :  Ramesh  <next  line>   20  :  Kiran   <next  line>   15  :  Amar   <next  line>  18  :  Sita  <next  line>



'''
1) for  x  in  dictionary:
	       print(x)
    Is  the  above  for  loop  valid ?  --->  Yes  becoz  keys()  method  is  executed   by  default

2) for  x  in  dictionary:
	       print(x)
    How  is  the  above  for  loop  interpreted ?  --->  for  x  in  dictionary . keys()
     																                            print(x)

3) for  x , y  in  dictionary . keys():
			 print(x , y)
    Is  the  above  for  loop  valid  ?  ---> No  becoz  two  variables  are  not  permitted  for  keys()  method

4) for  x , y  in  dictionary . values():
			 print(x , y)
     Is  the  above  for  loop  valid  ?  ---> No  becoz  two  variables  are  not  permitted  for  values()  method

5) When  are  two  variables  permitted  in  for  loop ?  ---> Only  for  items()  method

6) for  x , y  in  dictionary:
	       print(x , y)
    Is  the  above  for  loop  valid ?  ---> No  becoz  the   above  for  loop  is  interpreted  as   for  x , y  in   dictionary . keys():
							                                  and  two  variables  are  not  permitted  for  keys()  method

7) a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
    for  x  in   a . items():
			print(x[0] , x[1] , sep = '...')
    What  is  'x'  in  the  above  for  loop ?  --->  Each  tuple  of  the  list  in  dict_items  object
    What  are   x[0]  and  x[1]  ? --->  Elements  of  each  tuple

8) a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
    for  x  in   a . items():
			print(*x)
    What  does  *x  do ? --->  Unpacks  tuple  into  elements

9) a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
     for  x  in  a . keys():
	     print(x)
    Iteration         x
    -------------------------
        1                   10
        2                  20
        3                  15
        4                  18

10) a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
     for  x  in  a . values():
	        print(x)
    Iteration     x
    -----------------------
         1             'Ramesh'
         2             'Kiran'
         3             'Amar'
         4             'Sita'

11) a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
     for  x   in  a . items():
	        print(x)
    Iteration         x
  ------------------------------------
           1              (10 , 'Ramesh')
           2              (20 , 'Kiran')
           3              (15 , 'Amar')
           4              (18 , 'Sita')

12) a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
      for  x , y  in   a . items():
	       print(x , y , sep = ':')
     Iteration      x        y
    -----------------------------
          1               10        'Ramesh'
          2              20       'Kiran'
          3              15       'Amar'
          4              18       'Sita'

13) a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
     for  x  in  a . keys():
	       print(x , a[x])
    Iteration         x       a[x]
    -----------------------------------
         1                 10        'Ramesh'
         2                20        'Kiran'
         3                15        'Amar'
         4                18        'Sita'
'''
