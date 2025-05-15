#  Find  outputs
from  cal  import   y , sub , mul
#print(x) #  Error :  No  'x'  in current module
print(y) # 200
#print(add(10 , 7)) #  Error  :  No  add()  in current module
print(sub(10 , 7))  # 3
print(mul(10 , 7))   #   70
#print(div(10 , 7)) # Error :  No  div()   in current module
#a = c1() #  Error :  Np  class c1  in current module




'''
from  cal  import   y , sub , mul
Why  are  x ,  add , mul  and  c1  not  imported  even  though  they  are  in  __all__  list ?  --->
																													Since  *  is  not  used  in  import  clause
'''