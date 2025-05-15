#  max()  and  min()   functions  demo  program
from  builtins  import   max , min   #  Optional  becoz  they  are  automatically  imported
print(max(10.8 , 20.6))  #  20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))  #   5.9
print(max(25 , 10.8)) #   25
import  builtins #  Mandatory  becoz  module  is  not  imported  automatically
print(builtins . max(10 , 20 , 30))  #   30
print(builtins . min(10 , 20 , 15 , 5 , 12))  #   5



'''
How  many  arguments  can  max()  and  min()  functions  take  ?  --->
																			Any  number  of  arguments  becoz  they  are   var-arg  functions
'''
