'''
(Home  work)
Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)

Let  input  be   RamA raO
What  is  the  output ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order

Hint: Use  get()  method
'''
a=input("enter the srtring:")
b=a.upper()
for i in a:
    set = {}
    if i.isalpha():
        set[i]=set.get(i,0)+1
sorted_set=dict(sorted(set.items()))
print(sorted_set)