#  Anonymous  object  demo  program
_ = 25  #  Anonymous   object  contains   25
print(_) #   Value  of  nameless  object  i.e.  25
print(type(_)) #   <class  'int'>
a , _ , c = 10 , 20 , 30   #  Multiple  assignment
print(a)  #10
print(_) #  20
print(c) #  30
for  _  in  range(5):
	print(_ , 'Hello')  #   0  <space>  Hello  <next  line>   1  <space>  Hello  <next  line>   2  <space>  Hello  <next  line>   3   <space>  Hello  <next  line>   4   <space>  Hello  <next  line>




'''
1) What  is   _   called ?   --->  Anonymous  object  (or) Nameless  object

2) How  many  total  objects  are  in  the  above  program ?  --->  1 + 3 + 5 = 9
     How  many  objects  alive  are  in  the  above  program ?  --->   3  i.e.  a , c  and  nameless  object

3) How  many  objects  are  nameless  in  the  above  program ?  --->  One  at  a  time

4) In  other  words,  old  nameless  object  is  lost  every  a  new  nameless  object  is  created
'''
