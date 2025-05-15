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
a = eval(input('Enter any list: '))  #  [10 , 20 , 15 , 12 , 18 , 15 , 19 , 15 , 14]
x = eval(input('Enter the element to be searched : '))  #   15
for  i  in  range(len(a)):
	if  a[i] == x:
		print('Found  at   index  :  ' ,  i)
		break
else:
	print('Not  Found')


'''
1) What  are  the  two  issues  when  break  is  omitted ?  --->
	a) 'x'  is  searched  in  rest  of  the  list  even  though  it  is  already  found  in  the  list
	   (program  execution  becomes  slow)
	b) Not  Found  msg  is  also  printed  after  for  loop  terminates

2) What  is  the  issue  when  else  is  omitted ?  --->  Both  Found  and  Not  Found  messages  will  be  printed

3) What  is  the  issue  when  else  is  indented  with  if  ?  --->
										Not  Found  msg  is  printed  in  each  iteration  of  for  loop  until  element  is  found  in   the  list
'''
