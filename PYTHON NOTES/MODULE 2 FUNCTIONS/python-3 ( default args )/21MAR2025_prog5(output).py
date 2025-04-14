#  Find  outputs (Home  work)
def  f1():
        a = 10  #   Creates  Lv   with value  10
        #global  a # error  becoz  Lv  'a'  already  exists
        print(a)   # Lv  i.e.  10
        global  b  #  Treats  'b'  as  Gv  to  f1()  function
        b = 20  #   Creates  Gv   with value  20
# End  of  f1()  function
f1()
#print(a) # error  becoz  there  is  no  Gv  'a'
print(b) #  Gv   i.e.  20

'''
10
20
'''

'''
global  keyword  can  be  used  any  where  in  the  function  but  not  necessarily  at  the  begining  of  the  function
'''
