# Find  outputs
b = 10
#a = b += 5    #   a = No result  throws  error
print(b)    #   10



'''
1) a = b += 5
    Why  is  +=  operator  first  evaluated ?  ---> Since  assignment  operators  are  evaluated  from  right  to  left

2) a = b += 5
    What  is  the  result  of  b += 5  ?   ---> Adds  5  to  object  'b'  and   the  result  is  nothing

3) What  is  the  issue  with  a = b += 5 ?  --->  a = nothing  throws  error
'''
