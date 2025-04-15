'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10,20,15,18,19,15,17,20,15,14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

Hint: Use  remove()  method
'''

k=list(map(int, input("Enter list elements separated by spaces: ").split(',')))

print(k)
p=int(input("enter the elememt to remove:"))
while p in k:
        k.remove(p)
print(k)