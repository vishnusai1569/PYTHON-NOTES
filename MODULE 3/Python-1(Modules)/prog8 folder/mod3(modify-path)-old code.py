# sys . path  demo   program
import  sys
print(len(sys . path)) #  6
sys . path .  append('//Users//vishnusai//Desktop//VISHNU//PYTHON NOTES//MODULE 3//Python-1(Modules)//prog5 folder') # Appends  a  new  directory  to  sys.path
print(len(sys . path)) #7
import  cal  #  Success  :  cal.py  is  found  in  c:\sairam  folder
print(cal . x)
print(cal . y)
print(cal . add(10 , 7))
print(cal . sub(10 , 7))
print(cal . mul(10 , 7))
print(cal . div(10 , 7))
a = cal . c1()
a . m1()