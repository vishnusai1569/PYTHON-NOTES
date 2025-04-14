# Find outputs  (Home  work)
def  disp(a , b):  #  Discarded  becoz  another  function  is   defined  with  same  name
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):#  Discarded  becoz  another  function  is   defined  with  same  name
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):  #   Recognized
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 3-argument  function  :  <space>  10  <space> 20  <space> 30
#disp(40 , 50 , 60 , 70) # error  due  to  excess  arguments
disp(80 , 90) # 3-argument  function  :  <space>  80   <space>  90  <space>  25
