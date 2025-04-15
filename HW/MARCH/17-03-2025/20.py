'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
a=int(input("enter the no of emp:"))
b={}
for i in range(a):
    k=input("enter the empname:")
    p=int(input("enter the salary:"))
    b[k]=p
print(b)