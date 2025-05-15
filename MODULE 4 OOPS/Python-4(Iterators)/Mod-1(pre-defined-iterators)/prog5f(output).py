# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
for  x  in  reversed(a . keys()):  #  'x'  is   each  key  yielded  by  reversed   iterator
	print(x)  #   18  <next  line>  15 <next  line> 20  <next  line>  10  <next  line>
	time.sleep(1)
print('Values  in  reverse  order')
for  x  in  reversed(a . values()):  #  'x'  is   each  value   yielded  by  reversed  iterator
	print(x)  # Kiran  <next  line>  Rajesh<next  line>  Sita  <next  line>  Rama rao  <next  line>
	time.sleep(1)
print('Tuples  in   reverse  order')
for  x  in  reversed(a . items()):  #  'x'  is  each  tuple   yielded  by  reversed   iterator
	print(x)  #   (18 , 'Kiran')  <next  line>  (15 , 'Rajesh')  <next  line>  (20 , 'Sita')  <next  line>  (10 , 'Rama  rao')  <next  line>
	time.sleep(1)
print('Elements  of  each   tuple  in  reverse  order')
for  x ,  y  in  reversed(a . items()):  #  'x'   and  'y'  are  elements  of  each  tuple  yielded  by  reversed   iterator
	print(x , y , sep = '...')  #   18 ...  Kiran   <next  line>   15 ...  Rajesh   <next  line>   20  ... Sita   <next  line>   10  ...  Rama  rao   <next  line>
	time.sleep(1)
print('Keys  and  values  in   reverse   order')
for x in reversed(a . keys()): #  'x'  is   each  key  yielded  by  reversed   iterator
	print(x , a[x] , sep = '...')  #   18 ...  Kiran   <next  line>   15 ...  Rajesh   <next  line>   20  ... Sita   <next  line>   10  ...  Rama  rao   <next  line>
	time.sleep(1)