# Save  in  any  file  of  cwd
import  p1 . mod1 , p1 . mod2  #   How  to  import  mod1  and  mod2  of  package  p1  with  import  statement
print(p1 . mod1 . x)  #  How  to  print  variable  'x'  of   mod1  in  package  p1
p1 . mod1 . f1()  #  How  to  call  function  f1()  of   mod1  in  package  p1
a = p1 . mod1 . c1()
a . m1()  #  How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(p1 . mod2 . x)  # How  to  print  variable  'x'  of   mod2  in  package  p1
p1 . mod2 . f1()  #  How  to  call  function  f1()  of   mod2  in  package  p1
a = p1 . mod2 .  c1()
a . m1()  # How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1



'''
1) What  does  import  p1  do ?  --->  Imports  package  p1  but  not  modules  of  the  package  p1

2) import  p1
    Is  p1 . mod1 . x  valid ?  --->  No  becoz  mod1  is  not  imported  and  hence  mod1  can  not  be  used

3) import  mod1 , mod2
    Where  are  mod1  and  mod2  searched ?  --->  In  cwd
    What  is  the  issue  with  the  above  statement ? --->
												There  are  no  mod1  and   mod2  in  cwd  and  hence  throws  ModuleNotFoundError

4) import  p1 . mod1
    import  p1 . mod2
    How  to  reduce  the  above  two  statements  to  a  single  statement ?  --->	import  p1 . mod1 , p1 . mod2

5) import  p1 . mod1 , p1 . mod2
    Where  are  mod1  and  mod2  searched ?  --->  In  sub-directory  p1  but  not  in  cwd
'''