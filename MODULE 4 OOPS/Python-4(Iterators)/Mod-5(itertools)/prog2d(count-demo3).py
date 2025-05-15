#  Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t')
        print()
#end  of  the  function
a = count(start = 10)  #  1st  count  object
disp(a)  # 10 <tab> 11 <tab> 12 <tab> 13 <tab>
b = count(start = 10 , step = 5)   #  2nd  count  object
disp(b) # 10 <tab> 15 <tab> 20 <tab> 25 <tab>
c = count(start = 10 , step = -2.5)    #   3rd  count  object
disp(c)  #  10 <tab> 7.5 <tab> 5 <tab> 2.5 <tab>
d = count()   #  4th   count  object
disp(d) #  0 <tab> 1 <tab> 2 <tab> 3 <tab>