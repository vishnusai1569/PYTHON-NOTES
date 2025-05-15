'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Use  for  loop
'''
import   time
class   Power:
	def  __init__(self , begin , end):
		self . begin =begin
		self . end  = end
	def  __iter__(self):
		print('Iterator  for  Powers  of  2')
		return  self
	def  __next__(self):
			if  self . begin  <=  self . end:
				result  =  2  **  self . begin
				self . begin  +=  1
				return  result
			raise  StopIteration
#End  of  the  class
p = Power(0 , 7)  #  Object  is  initialized  with  begin = 0 , end = 7  by  constructor
for  x   in   p:  #  'x'  is  each  element  returned  by  __next__()  method  of  class  Power
	print(x)  #  1  <next line>  2  <next line>  4  <next line>  8  <next line>  16  <next line>  32  <next line>  64  <next line>  128  <next line>
	time . sleep(1)
print('End')


'''
Iterator  for  Powers  of  2
1
2
4
8
16
32
64
128
End
'''