# Find  outputs  (Home  work)
x = 30
def   disp():
        print('disp  function  of  same  module ')
class   c1:
    def   m1(self):
        print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)
disp()
a = c1()
a . m1()