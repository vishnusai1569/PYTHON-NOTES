# What  are  the  drawbacks  of  sequences ?
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:
	print(y)



'''
1) What  are  the  two  drawbacks  of  seqeunces ?  --->
    a) Waiting  time:  When  there  are  too  many  elements,  representing  all  of  them  in  sequence  takes  longer  time
	b) Memory  Error:  When  there  are  too  many  elements,  there  may  not  be  enough  memory  to
	                               represent  all  of  them  in  sequence

2) When  are  sequences  not  recommended  ?  ---> When  there  are  too  many  elements

3) In  other  words  sequences  are  recommended  only  when  there  are  few  elements
'''
