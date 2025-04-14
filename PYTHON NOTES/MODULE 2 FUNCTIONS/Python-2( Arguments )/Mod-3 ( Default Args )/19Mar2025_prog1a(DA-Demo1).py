# Default  arguments  demo  program
def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))  #  'a'  is  100 , 'b'  is  default  value  20 , 'c'  is  default  value  30  and  result  is  150
print(add(100 , 200))  #  'a'  is  100 , 'b'  is  200 , 'c'  is  default  value  30  and  result  is   330
print(add(100 , 200 , 300))  #  'a'  is  100 , 'b'  is 200 , 'c'  is  300  and  result  is   600
print(add(100 , c = 200)) #  320
print(add(c = 100 , b = 200 , a = 300))  # 600
print(add(c = 100 , a = 200)) #   320
#print(add())  #  Error  :  Arg is  not  passed  for  'a'
#print(add(a = 100 , 200))  #  Error : PA  after  KA
#print(add(100 ,  , 300)) #  Error  :  2  commas
#print(add(100 ,  b , 300))  # Error : object  'b'  does  not  exist
