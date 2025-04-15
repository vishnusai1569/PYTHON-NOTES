#  How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)
print(type(z))
print(z)
print('Iterate  zip  object  with   next()   function')
while True:
    try:
        print(next(z))
        time.sleep(0.5)
    except:
        break

print('Iterate  zip  object  with  _next_  method')
z = zip(a , b)
while True:
    try:
        print(z.__next__())
        time.sleep(0.5)
    except:
        break

print('Iterate  zip  object  with   for  loop')
for item in zip(a , b):
    print(item)
    time.sleep(0.5)

print('Iterate  elements  of  each  tuple  in  zip  object')
for x,y in zip(a , b):
    print(x,y,sep="    ")
    time.sleep(0.5)

print('Unpacks  zip  object  with   *  operator  :  ' , *zip(a,b))
print()

print('zip   object  in  the  form  of   list  :  ' ,  list(zip(a,b)))
print()

print('zip   object  in  the  form  of   dictionary :  ' , dict(zip(a,b)))
