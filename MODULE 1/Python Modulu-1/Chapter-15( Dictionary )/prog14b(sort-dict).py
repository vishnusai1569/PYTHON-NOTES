'''
Gift : Rs. 1000
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  --->{5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function
'''
a = eval(input('Enter  dictionary  :  '))
b = a . items()
c = sorted(b)
print(dict(c))


'''
How  to  sort  dictionary ?  --->   dict(sorted(dict . items()))
'''
