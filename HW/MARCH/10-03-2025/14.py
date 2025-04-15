'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result

Hint:  Use  split()  method
'''
k=input("enter the input:").split('+')
sum=0
for i in range(len(k)):
    sum=sum+eval(k[i])
print(sum)