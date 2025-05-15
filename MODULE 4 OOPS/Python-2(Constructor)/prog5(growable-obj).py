
# Find  outputs (Home  work)
class   c1:
        def   __init__(self):
                self . a = 10
        def   m1(self):
                self . b = 20
#End  of  class  c1
class   c2:
        def  m3(self):
                x . e = 50
# End  of  class  c2
def   f1():
        x . c = 30
#  End  of  function  f1
x = c1()  #  Constructor  adds  variable  'a'  to  object  'x'   with  value   10
print(x . __dict__)   #   {'a' : 10}
x . m1()   #  Method  adds  variable  'b'  to  object  'x'   with  value  20
print(x . __dict__)   #   {'a' : 10 , 'b' :  20}
f1()  #  Function  adds  variable  'c'  to  object  'x'   with  value  30
print(x . __dict__)   #   {'a' : 10 , 'b' :  20 , 'c' : 30}
x . d = 40  #  Adds  variable  'd'  to  object  'x'   with  value  40
print(x . __dict__)   #   {'a' : 10 , 'b' :  20 , 'c' : 30 , 'd' : 40}
y = c2()  #  Empty  object  :  There  is  no  constructor  in  class  c2
y . m3()  #  Method  of  class  c2  adds  variable  'e'  to  object  'x'   with  value   50
print(x . __dict__)   #   {'a' : 10 , 'b' :  20 , 'c' : 30 , 'd' : 40 , 'e' : 50}
z = c1()   #  Constructor  adds  variable  'a'  to  object  'z'   with  value   10
print(z . __dict__)   #   {'a' : 10}



'''
1) How  many  variables  are  in  object  'x'  finally --->  Five  i.e.  a = 10 , b = 20 , c = 30 , d = 40 , e = 50

2) How  many  variables  are  in  object  'y'  --->  Zero  i.e.  Empty  object

3) How  many  variables  are  in  object  'z'  --->  Single  i.e.  a = 10

4) Both  'x'  and  'z'  are  c1  class  objects

5) In  general,  all  c1  class  objects  may  not  contain  same  number  of  variables

6) x = c1()
    Is  x . m3()  valid ? --->  No  becoz  there  is  no  m3()  method  in  class  c1  as  'x'  is  c1  class  object

7) The  above  program  demonstrates  that  python  object  is  growable

8) Where  can  variables  be  added  to  the  object  ?  ---> Any  where  in  the  program
									i.e.  In  Constructor , method , function , outside  the  class  and  in  some  other  class
'''