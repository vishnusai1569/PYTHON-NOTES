# Find  outputs  (Home  work)
class  father:
        def  height(self):
                print('Father  Height')
class  mother:
        def  color(self):
                print('Mother  Color')
class  child(mother , father):
        def  qualification(self):
                print('Child Qualification')
# End  of  the  class
c  =  child()
c . qualification()  #   Method  of  child  class  is  executed  becoz  'c'  is  child  class  object
c . color()   #   Method  of  mother  class  is  executed  becoz   there  is  no  m1()  in  child  class
c . height()  #   Method  of  father  class  is  executed  becoz   there  is  no  m1()  in  child   and  mother  classes
#c . m1() #  Error  :  There  is   no m1 method in  child , mother   and  father  classes

'''
Child Qualification
Mother  Color
Father  Height


1) What  is  the  order  in  which  a  method  is  searched ?  --->  In  child , mother  and  father  classes

2) In  other  words,  order  in  which  classes  are  derived  plays  a  key  role  but  not  the  order  in  which
    classes  are  defined
'''