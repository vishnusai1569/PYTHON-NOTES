'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

k= input("enter the string:")
vowels='AEIOU'
c=""
for i in k:
    i=i.upper()
    if i in vowels and i not in c:
        c=c+i
print(c)