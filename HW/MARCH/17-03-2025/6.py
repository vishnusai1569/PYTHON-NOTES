'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
   What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
a=input("enter the string:")
b=a.upper()
k="AEIOU"
set=set()
for i in b:
    if i in k:
        set.add(i)
print("".join(set))

