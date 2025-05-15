# Find outputs  (Home  work)
class    c1:  #  Discarded  becoz  a  function  is  with  same  name  later
        def  _init_(self):
                print('Constructor')
def  c1(x):  #  Recognized
        print('Function : ' , x)
# End  of  class  c1
#a = c1()  #  Error :  Arg  is  not  passed  for  arg  'x' of  function c1()
b = c1(25)  #  Executes  function  c1()  which  returns  None  by  default
print(b)  #  None

'''
Function :  25
None
'''