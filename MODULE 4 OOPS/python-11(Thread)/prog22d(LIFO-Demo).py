#  Find  outputs  (Home  work)
from   queue  import  LifoQueue
stack = LifoQueue()
for  i  in  range(1 , 6):
	stack . put(10 * i)  #   Inserts  10 , 20 , 30 , 40  and  50  into   stack  object
print('Deleted  elements')
while  not   stack . empty():  #   Execute  until  stack  object   is  empty
        print(stack . get()) #  50  <next  line>  40  <next  line>  30  <next  line>  20  <next  line>  10  <next  line>
print(stack . get())  #   main  thread  waits  as   stack  is   empty
print('End')  # Not  executed