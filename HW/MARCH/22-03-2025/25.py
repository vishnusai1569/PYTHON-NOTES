#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1()#f1    function
f2()#f2    function
print(f1  is  f2)#false
f2 = f1
f2()#f1    function
print(f1  is  f2)#true
f2 = f1()
print(f2)#f1    function,None
#f2()error