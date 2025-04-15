#  pop()  method  demo  program
a = [10 , 20 , 15 , 18 , 12]
print(a . pop(2))  #  Removes  element  at  index  2  and  returns  the  deleted  element  i.e.   15
print(a) #  [10,20,18,12]
#print(a . pop(len(a)))  #  Error  becoz  index  4  does  not  exist
print(a . pop(-3)) #  Removes  element  at  index  -3  and  returns  the  deleted  element  i.e.   20
print(a)  # [10,18,12]
#print(a . pop(-4))   #  Error  becoz  index  -4  does  not  exist
print(a . pop())  #  Removes   last  element   of  the  list   and  returns  the  deleted  element  i.e.  12
print(a) #   [10,18]
b = []
#b . pop()  #  Error  becoz  list 'b'  is  empty


'''
pop()   method
------------------
1) What  does  pop(index)  do ?  --->  Removes  element  at  the  specified  index  and  returns  the  deleted   element

2) What  is  the  argument  of  pop()  method ?  --->  Index  of  the  element  to  be  removed

3) What  does  pop(invalid-index)  do  ?  --->  Throws  IndexError

4) What  does  pop(No  args)  do ?  --->  Removes  last  element  of  the  list  and  returns  the  deleted  element

5) How  many  arguments  can  pop()  method  take ?  --->  1  (or)  0

6) What  does  pop(No  args)  do  when  list  is  empty ?  --->  Throws  error

7) list . pop(index)
    del  list[index]
    What  is  the  difference  between  the  above  two  statements ?  --->
											del  operator  removes  element  but  does  not  return  the  deleted  element
											whereas  pop()  method  not  only  deletes  element  but  also  returns  the  deleted  element
'''
