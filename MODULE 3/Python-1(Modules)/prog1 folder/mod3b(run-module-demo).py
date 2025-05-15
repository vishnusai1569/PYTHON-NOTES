

#  Find  outputs  (Home  work)
import   runpy
print('Before')
runpy . run_module('mod2')   #  How  to  run  mod2  without  import
#print(mod2 . x)  #  Error  : mod2  is  not  imported
#mod2 . f1()  #  Error  : mod2  is  not  imported
print('After')
#run_module('mod2')  #  Error  :   There  is  no  run_module()  function  in  current  module




'''
runpy . run_module('mod2')
Are  functions  of  mod2  executed ?  --->  No  becoz  they  are  not  called  by  mod2
Are  methods  of  class  c1  in  mod2  executed ?  --->  No  becoz  they are  not  called  by  mod2
'''