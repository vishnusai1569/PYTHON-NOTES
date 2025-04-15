'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
k= input("input:")
b=k.split()
sum=''
for i in b:
    sum=sum+i[::-1]+" "
print(sum)
