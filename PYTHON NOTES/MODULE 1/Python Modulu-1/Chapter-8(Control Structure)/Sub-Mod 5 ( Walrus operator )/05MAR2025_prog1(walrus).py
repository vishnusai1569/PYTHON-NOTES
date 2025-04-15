#  Walrus   operator (:=)  demo  program
print(a := 25)  #  Value    of  'a'  is  25  and  result  of  a := 25 is  also  25
#print(a = 25)  #  print(No  result)  throws   error  beoz  value  of  'a'  is  25  but  result  of  a = 25  is  nothing
print(a)   # 25
print(a := 6 + 7)  #  Value    of  'a'  is   13   and  result  of  a := 13   is  also   13
print(a) #   13
print((a := 6) + 7)  #  print(6 + 7)  --->  13
print(a)  #  6
#print((a = 6) + 7)  #  print(No  result  + 7)  throws  error


'''
1) What  is  the  similarity  between  a :=  25  and  a =  25 ?  --->  Assigns  25  to  object  'a'

2) What  is  the  difference  between  a := 25  and  a =  25 ?  --->  Result  of  a := 25   is  25  but
																	                                    result  of  a =  25  is  nothing

3) a = 25
    print(a)
    How  to  reduce  the  above  two  statements  to  a  single  statement ?  --->  print(a := 25)

4) When  is  walrus  operator  introduced  to  python  ?  --->  From  python  3.8

Note:
What  is  the  result  of  a = 25  in  other  languages ?  --->  25
'''
