'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  ---> ADKPZ13579

1) Hint:  sorted()  function , isalpha() , isdigit()  and   join()  method
'''
k=input("enter the string:")\
sum=''
m=''
for i in range(len(k)):
    if k[i].isalpha():
        sum=sum+k[i]
    elif k[i].isdigit():
        m=m+k[i]
    else:
        print("enter only alpha and numeric:")
        exit()
r="".join(sorted(sum)+sorted(m))
print(r)
