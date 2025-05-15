#  Find  outputs
from   itertools    import    count
cnt = count() #   Empty   object
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)    #  Empty  object
print('while  loop')
while   True:
        try:
                print(next(z1))  #   (0 , 10)  <next  line>  (1 , 20)  <next  line> (2 , 15)  <next  line>  (3 , 18) <next  line>
        except:
                break
z2 = zip(cnt , list)  #   2nd    object  to  iterate  again
print('for  loop')
for  x   in    z2:
        print(x)  #   (5 , 10)  <next  line>  (6 , 20)  <next  line> (7 , 15)  <next  line>  (8 , 18) <next  line>
z3 = zip(cnt , list)  #    3rd   object  to  iterate  again
print('Next  element :  ' , next(z3))  #  (10 , 10)
print('*z3 :  ' ,  *z3) #  (11 , 20)  <space>   (12 , 15)  <space>  (13 , 18)
z4 = zip(cnt , list)   #   4th   object  to  iterate  again
print('Next  element  :  ' , next(z4))  #   (15 , 10)


'''
1) Why  is  (4 , 10)  not  printed  by  for  loop  ?  --->
												      Since  4  is  already  yielded  by  next(z1)  but  not  printed  as  list  got  exhausted

2) Why  is  (9 , 10)  not  printed  by  next(z3) ?  ?  --->
													 Since  9  is  already  yielded  by  for  loop  but  not  printed  as  list  got  exhausted

3) Why  is  (14 , 10)  not  printed  by  next(z4) ? --->
                                                           Since  14  is  already  yielded  by  *z3  but  not  printed  as  list  got  exhausted
'''