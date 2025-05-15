#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list) #  1st  zip  object
print('while  loop')
while   True:
        try:
                print(next(z1))  #   (0 , 10)  <next  line> (1 , 20)  <next  line>  (2 , 15)  <next  line>  (3 , 18)   <next  line>
        except:
                break
z2 = zip(list , cnt)  #  2nd  zip  object
print('for  loop')
for  x   in    z2:
        print(x)   #   (10 , 5)  <next  line>  (20 , 6)  <next  line>  (15 , 7)  <next  line>  (18 , 8)  <next  line>
z3 = zip(cnt , list)  #  3rd  zip  object
print('Element :  '  , next(z3))  #  Element :  (9 , 10)
print('*z3 : ' , *z3)  #   (10 , 20) <space> (11 , 15) <space> (12 , 18)
z4 = zip(list , cnt) #  4th  zip  object
print('Element :  ' , next(z4))   #  Element :  (10 , 14)