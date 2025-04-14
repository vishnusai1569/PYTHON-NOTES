# Find  outputs
def    f1():
        return  10
        return  20  #  Skipped  due  to  return  10
        return  30  #  Skipped  due  to  return  10
# End  of  the  function
print('Begin')
x = f1()  #  x = 10
print(x)
print('End')
#return   100   #  Error :  return  outside  the  function


'''
Begin
10
End
'''
'''
1) return  10 , 20 , 30
    What  is  returned  ?  --->  A  tuple  of  3  elements  i.e. (10 , 20 , 30)

2) return  10
    return  20
    return  30
    What  is  returned ?  --->  Just  10  and  next  two  statements  are  skipped
'''
