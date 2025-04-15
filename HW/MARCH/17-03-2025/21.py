''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''

a=input("enter the list:")
b=a.split(",")
result={}
for i in b:
    key, value = i.split('=')
    key = key.strip()
    value = value.strip()
    result[key] = value
print(result)