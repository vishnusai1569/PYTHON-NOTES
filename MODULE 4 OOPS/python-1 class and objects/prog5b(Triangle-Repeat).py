

'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
from  prog5a   import  triangle
t = triangle() #   How  to  create  triangle  object
triangle . get(t)#  How  to  call  get()  method  in  another  way
triangle . test(t)  # How  to  call  test()  method  in  another  way
print('Area : ',  triangle . area(t) )  #   How  to  call  area()  method  in  another  way)
print('Perimeter: ', triangle . peri(t))  #   How  to  call  peri()  method  in  another  way



'''
1) from  prog5a  import  triangle
	What  are  imported ?  --->  triangle  class   and  the  if  statement  defined  outside  triangle  class

2) py  prog5a.py
    What  is  the  value  of  __name__  variable  wrt  the  above  command ?  --->
																									'__main__'  becoz   prog5a  is  directly  executed

3) from  prog5a   import  triangle
    What  is  the  value  of  __name__  variable  wrt  the  above  statement ?  ---> Module  name  i.e.   'prog5a'
     Is  if   statement  executed ?  --->  No  becoz  if  condition  is   false

*4) In  general, statements  outside   the  class  should  be  under  if  condition  so  that
      they  are  not   executed  when  the  program  (or)  module  is  imported

5) classes , functions  and  variables  defined  in  a  program  can  be  reused  by  a   different  program.
    This  is  possible  with  import  (or)  from  statement

6) import  prog5a
    What  are  imported ?  ---> prog5a  and  if  statement
     Is  triangle  class  imported ?  ---> No  becoz  members  are  not  imported
     How  to  use  triangle  class ?  --->  prog5a . triangle
'''