#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g) # Waiting  time  (or)  memory  error  due  to  too many  elements



'''
What  are  the  three  events  for  *g ?  --->
1) Generator  expression  is  fully  executed  without  stopping  in  the  middle
2) 0 ^ 2 , 1 ^ 2 , 2 ^ 2 , ....   are  stored  in  generator  object  'g'
3) Generator  object  is  unpacked  with  *  operator
'''
