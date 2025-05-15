#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
import  time
print('Odd  numbers  between  1  and  20')
f = filter(lambda  x :  x % 2 ==  1 ,  range(1 , 21))  #  Creates  an  empty  filter  object
for  y  in  f:
	print(y) #   1  <next  line>  3  <next  line>  5 <next  line>  7  <next  line>  9  <next  line>  11<next  line>  13 <next  line>  15  <next  line>  17  <next  line>  19  <next  line>
	time . sleep(1)



'''
1) What  is  'x' ?  --->  Each  element  of  range  object  i.e.  1  to   20

2) How  many  times  is  lambda  function  executed ?  --->  20  times  becoz  there  are  20  elements  in  range  object

3) How  many  times  is  for  loop  executed ?  --->  10  times  becoz  there  are  10  odd  numbers  between  1  and  20
'''