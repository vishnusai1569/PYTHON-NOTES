

# setattr() , getattr()  and  hasattr()  functions  demo  program
class  Emp:
        pass
# End of  the class
e = Emp()  #  Creates  empty  Emp  class  object
print(e . __dict__) #   { }
setattr(e , 'empno' , 25)  #  Adds  variable  empno  to  object  'e'  wiith  value   25  (same  as  e . empno = 25)
setattr(e , 'ename' , 'Rama  Rao')  #  Adds  variable  ename  to  object  'e'  wiith  value   'Rama  Rao'  (same  as  e . ename = 'Rama  Rao')
setattr(e , 'sal' , 10000.0)  #  Adds  variable  sal  to  object  'e'  wiith  value   10000.0 (same  as  e . sal = 10000.0)
setattr(e , 'sal' , 20000.0)  #  Modifies   e . sal  to   20000.0  (same  as  e . sal = 20000.0)
print(e . __dict__)  #  {'empno' : 25 , 'ename' : 'Rama  Rao' ,  'sal' : 20000.0}
print('Emp  number  :  ' , getattr(e , 'empno'))  #  Returns  value  of  e . empno  (same  as  print(e . empno))
print('Emp  name    :  ' , getattr(e , 'ename'))   #  Returns  value  of  e . ename  (same  as  print(e . ename))
print('Salary  :  ' , getattr(e , 'sal'))   #  Returns  value  of  e . sal  (same  as  print(e . sal))
#print('Gender  :  ' , getattr(e , 'gender'))   #   Error :  No  gender  variable  in   object  'e'
print(hasattr(e , 'empno'))  #   True :  Variable  empno   exists  in   object  'e'
print(hasattr(e , 'ename'))   #   True :  Variable  ename   exists  in   object  'e'
print(hasattr(e , 'sal'))   #   True :  Variable  sal  exists  in   object  'e'
print(hasattr(e , 'gender'))   #   False :  Variable  gender  does  not  exist  in   object  'e'