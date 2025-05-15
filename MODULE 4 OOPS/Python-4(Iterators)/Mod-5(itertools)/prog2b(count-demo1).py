# Find   outputs
from  itertools  import  count
c = count()   #  Empty  object
print('While  loop')
while   True:
        x = next(c)
        if   x > 9:
                break
        print(x)  #  0  to  9
# End  of  while  loop
print('For  loop')
for  x  in   c:
	if  x  >  20:
		break
	print(x)  #  11  to   20
# End  of  for  loop
print('Element :  ' , next(c))  #   22
print(*c)  #   MemoryError


'''
1) Why  is  10  not  printed  by  while  loop ?  --->  Since  loop  is  broken  after  10  is  yielded

2) Why  is  for  loop  yielding  from  11 ?  --->  Since  10  is  already  yielded  by  while  loop

3) Why  is  for  loop  not  printing  21  ?  --->  Since  loop  is  broken  after  21  is  yielded

4) Why  is  next(c)  yielding  22 ?  --->  Since  21  is  already  yielded  by  for  loop

5) Why  *c   throws  memory  error ?  --->   Since  object  can  not  hold  infinite  number  of  elements  i.e.  23  to  infinity
'''