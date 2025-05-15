# Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3)) #  'x'  is  3 , 'a'  is   default   value  []  and  result  is  [0 , 1 , 4]
print(f1(4 , [10 , 20 , 15 , 18])) # #  'x'  is  4 , 'a'  is   [10,20,15,18]  and  result  is  [10 , 20 , 15 , 18 , 0 , 1 , 4 , 9]
print(f1(5)) #  'x'  is  5  , 'a'  is   default   value  []  and  result  is  [0 , 1 , 4 , 9 , 16]
print(f1(a = [100 , 200 , 300],   x = 6 ))  #  'x'  is  6  , 'a'  is    [100 , 200 , 300]  and  result  is  [100 , 200 , 300 , 0 , 1 , 4 , 9 . 16 , 25]
print(f1(6))  #  'x'  is  6 , 'a'  is   default   value  []  and  result  is  [0 , 1 , 4 , 9 . 16 , 25]
