#  Find  outputs
import  cal
print(cal . x)  # 100
print(cal . y) # 200
print(cal . add(10 , 7))  # 17
print(cal . sub(10 , 7)) # 3
print(cal . mul(10 , 7))  # 70
print(cal . div(10 , 7)) # 1.4
a = cal . c1() # creates class object
a . m1()

'''
100
200
17
3
70
1.4
m1 method
'''

'''
1) We  can  use  all  the  members  of  cal  module  becoz  cal  module  is  imported

2) It  doesn't  matter  what  __all__  list  contain  becoz  module  is  imported  but  not  members
'''