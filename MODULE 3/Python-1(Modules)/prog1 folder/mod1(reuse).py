#  How  to  reuse  mod2  from  mod1 ?
print('Before  import')
import  mod2   # How  to  import  mod2
#print(x)  #  Error  :  No  'x'  in  current  module
print(mod2 . x)  #   25
#f1()  #  Error :  No  f1()  in  current  module
mod2 . f1() # f1  function
print('After  import')
#import  mod4  #  ModuleNotFoundError  becoz  mod4  is  not  in  same  folder


'''
1) How  many  statements  are  imported  from  mod2 ?  --->  Four

2) How  many  statements  are  in  mod1  finally  ?  --->  1 + 4 + 1 = 6  statements

3) Where  is  mod2  located ?  --->  In  current  working  directory(i.e.  Same  folder)
'''