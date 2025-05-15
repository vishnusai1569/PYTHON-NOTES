'''
Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'''
import  time
class   c1:
	def   __init__(self , begin1 , end1):
		self . begin = begin1
		self . end = end1
	def   __iter__(self):
		print('__iter__  method')
		return  self
	def    __next__(self):
		if  self . begin  <=  self . end:
			value = self . begin
			self . begin += 1
			return  value
		raise  StopIteration
# End  of  the  class
if  __name__  ==  '__main__':
	a = c1(10 , 20)   #  Object  is  initialized  with  begin = 10 , end = 20   by  constructor
	for  x   in   a:  # 'x'  is  each  element  returned  by  __next__()  method  of  class  c1
		print(x)  #   10  <next  line>   11   <next  line>  12   <next  line>  ...   20   <next  line>
		time . sleep(1)
	print('End')  #   End


'''
__iter__  method
10
11
12
13
14
15
16
17
18
19
20
End
'''