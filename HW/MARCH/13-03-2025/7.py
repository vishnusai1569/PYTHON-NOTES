'''
Gift
Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
Let  input  be  [10,20,15,10,14,10,18,20,19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods
'''
k=list(map(int,input("enter the elements sep with ,:").split(",")))
print(k)
p=[]
for i in k:
    if k.count(i)==1:
        p.append(i)
print(p)
