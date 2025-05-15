# Find outputs (Home  work)
def  f1():
        global  a  #   'a' is  treated  as GV  to  f1()  function
        print(a) #  Gv  i.e.  11
        a += 1  #  Increments  Gv  i.e.  12
def  f2():
        global  a  #   'a' is  treated  as GV  to  f1()  function
        print(a)  #  Gv  i.e.  13
        a += 1  #  Increments  Gv  i.e.  14
# End  of  the  function
a = 10  # Gv
print(a)  #  Gv  i.e.  10
a += 1  #  Increments  Gv  i.e.  11
f1()
print(a)  #  Gv  i.e.  12
a += 1  #  Increments  Gv  i.e.  13
f2()
print(a)  #  Gv  i.e. 14


'''
10
11
12
13
14
'''
