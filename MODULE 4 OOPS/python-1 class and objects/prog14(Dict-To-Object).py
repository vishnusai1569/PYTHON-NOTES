

'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e = emp()
for  key , value  in  dict . items():
		   setattr(e , key , value)
for  key   in  dict . keys():
	          print(key , getattr(e , key) , sep = '...')



'''
1) for  key , value  in  dict . items():
		   setattr(e , key , value)
------------------------------------------------------------------------------------
Iteration      key               value                setatte(e , key , value)
-------------------------------------------------------------------------------------
       1             'Empno'         25                  e . empno = 25
       2             'Ename'        'Rama  Rao'    e . ename = 'Rama  Rao'
       3             'Sal'             10000.0          e . sal = 10000.0

2) First  for  loop  converts  dictionary  to  Emp  obj  'e'
    i.e.  contents  of  dictionary  are  copied  to  object  'e'

3) for  key   in  dict . keys():
	          print(key , getattr(e , key))
     ---------------------------------------------------------------------
       Iteration       key                         getattr(e , key)
     ----------------------------------------------------------------------
         1            'Empno'                  getattr(e , 'Empno')  returns  25
         2            'Ename'                 getattr(e , 'Ename')  returns  'Rama  Rao'
         3            'Sal'                      getattr(e , 'Sal')  returns  10000.0

4) Second  for  loop  prints  each  variable  of   object  'e'

5) for  key  in  dict . keys():  is  same  as   what ?  --->  for  key  in  dict:

6) for  key , value  in  dict:
    Is  the  above  for  loop  valid  ?  --->  No  becoz  two  variables  are  not  permitted  due  to  keys()  method
'''