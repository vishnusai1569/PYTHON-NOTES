# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans) # 1574



'''
1) What  is  the  result  of  filter ?  --->  20 ,  15 ,  18 ,  25

2) What  is  the  result  of  map ?  --->  400    225    324    625

3) What  is  the  result  of  reduce ?  --->  1574

4)  x         y        x  +   y
   --------------------------
    400    225      625
    625    324      949
    949    625      1574
'''