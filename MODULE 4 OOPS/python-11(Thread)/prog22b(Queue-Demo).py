#  Find  outputs  (Home  work)
from   queue   import  Queue
from  threading  import  *
q = Queue()
for  i  in  range(1 , 6):
	q . put(10 * i)  #   Inserts  10 , 20 , 30 , 40  and  50  into  object  'q'
print('Deleted  elements')
while  not   q . empty():  #   Execute  until  object  'q'  is  empty
        print(q . get())  #  10  <next  line>  20   <next  line>  30   <next  line>   40   <next  line>   50   <next  line>
print(active_count()) #  1
print(q . get()) #   main  thread  waits  as  object  'q'  is   empty
print('End')  #  Not  executed