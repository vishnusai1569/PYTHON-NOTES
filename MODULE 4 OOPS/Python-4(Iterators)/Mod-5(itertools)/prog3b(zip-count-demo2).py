#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt) #  1st  zip  object
print('While  loop')
while   True:
        try:
                print(next(z1))  #  (10 , 0)  <next  line>  (20 , 1)  <next  line>  (15 , 2) <next  line>  (18 , 3)  <next  line>
        except:
                break
z2 = zip(list , cnt)   #   2nd  zip  object  to  iterate  again
print('for  loop')
for  x   in    z2:
        print(x)  #   (10 , 4)  <next  line>  (20 , 5)<next  line> (15 , 6)  <next  line>  (18 , 7)  <next  line>
z3 = zip(list , cnt) #   3rd  zip  object  to  iterate  again
print('Next  element :  ' , next(z3)) #  Next  element : (10 , 8)
print('*z3 :  ' ,  *z3)  #   *z3 : (20 , 9) <space> (15 , 10) <space> (18 , 11)
z4 = zip(list , cnt)  #   4th   zip  object  to  iterate  again
print('Next  element  : ' ,  next(z4))  #  Next  element : (10 , 12)


'''
1) Why  is  for  loop  not  starting  from  (10 , 5) ?  --->  Since  list  got  exhausted  before  4  is   yielded  by  while  loop

2) Why  is  (10 , 9)  not  printed  by  next(z3) ? --->  Since  list  got  exhausted  before  9  is   yielded  by  for  loop

3) Why  is  (10 , 13)  not  printed  by  next(z4) ?  ?  --->  Since  list  got  exhausted  before  13  is   yielded  by  *z3
'''