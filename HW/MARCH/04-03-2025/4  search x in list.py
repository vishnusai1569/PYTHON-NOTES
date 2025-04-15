'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Note:  Do  not  use  index()  method

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  seacrhed ?  --->  Found  at  index  2

2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found

3) What  action  to  be  made  if  'x'  is  not  matched  with  the  current  element  of  list ?  --->  Compare  'x'  with  next  element  of  list

4) What  action  to  be  made  if  'x'  is   matched   with  list  element ?  --->  Print  found   message  along  with  index  and
																														  don't   search  in  rest  of  the  list

5) What  action  to  be  made  if  'x'  is   not  matched  with  all  the  elements  of  list ?  --->  Print  not  found   message

6) Hint: Use  for  loop
'''

a=[10,20,15,12,18]
k=int(input("enter the number to be searched :"))
for i in range(len(a)):
    if k==a[i]:
        print('found',i)
        break
else:
    print("not found")


