# Store  cal.py  in  c:\\sairam  folder  before  the  program  is  executed
import  sys
print(len(sys . path)) #  6
sys . path .  append('//Users//vishnusai//Desktop//VISHNU//PYTHON NOTES//MODULE 3//Python-1(Modules)//prog5 folder') # Appends  a  new  directory  to  sys.path
print(len(sys . path)) #7
import  cal  #  Success  :  cal.py  is  found  in  c:\sairam  folder
print(cal . x)  #  100
print(cal . y)  # 200
print(cal . add(10 , 7))  #  17
print(cal . sub(10 , 7))  #  3
print(cal . mul(10 , 7))  #  70
print(cal . div(10 , 7))  #  1.422
a = cal . c1()
a . m1()  #  m1  method


'''
6
7
100
200
17
3
70
1.4285714285714286
m1  method
'''