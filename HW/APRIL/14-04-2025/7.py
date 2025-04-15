#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r = reversed(a)
print(type(r))
print(r)

print('Iterate  reversed  object  with   next   function')
while True:
    try:
        print(next(r))
        time.sleep(0.5)
    except:
        break


print('Iterate  reversed  object  with   next   method')
r = reversed(a)
while True:
    try:
        print(r.__next__())
        time.sleep(0.5)
    except:
        break


print('Iterate  reversed  object  with   for  loop')
for item in reversed(a):
    print(item)
    time.sleep(0.5)

print('Unpack  reversed  object  with   *  operator :   ' ,*reversed(a))
print()
print('reversed  object  in  the  form   of  list  :  ' ,  list(reversed(a)))
print('Reverse  string   :   ' , "".join(reversed(a)))
#  Write all  the  outputs  here