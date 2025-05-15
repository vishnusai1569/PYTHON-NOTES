# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) #  'a'  is  30 , 'b'  is  40  and  result  is  70
print(add()) # a is default   value  10 , b is default   value  20   and  result  is  30
print(add(a = 50)) # a is  50 , b is default  value  20   and   result  is  70
print(add(b = 60 , a = 70)) # a is 70 and b is 60   and  result  is   130
#print(add(80 , 90)) #  Error  due  to  pa's


# Send  only  keyword  arguments  to  the  function  due  to  *  in  the  function  header
