a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a)

print('Each  inner  list   of   outer  list  without  indexes')
#How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
for x in a:
	print(x)

print('Elements  in  the  form   of  matrix   without  using  indexes')
#How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
for x in a:
	for y in x:
		print(y,end=" ")
	print()

print('Elements  in  the  form   of  matrix  using  indexes')
#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)
for i in range(len(a)): #0 1 2
	for j in range(len(a[i])):
		print(a[i][j] , end = '\t')
	print()



'''
matrix   style
----------------
10    20
30    40   50
60    70   80   90
'''