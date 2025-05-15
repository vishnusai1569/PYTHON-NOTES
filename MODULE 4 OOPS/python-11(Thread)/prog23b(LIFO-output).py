#  Find  outputs  (Home  work)
from  queue  import   LifoQueue
stack = LifoQueue()
stack . put(('Hyd' , 10))   # Inserts  5  tuples  into  stack
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
while   not  stack . empty():  #  Executed  until  stack  is  empty
        print(stack . get())  #  ('Mumbai', 12)  <next  line>  ('Pune', 5)  <next  line>  ('Chennai', 15)  <next  line>  ('Delhi', 20)  <next  line>  ('Hyd', 10) <next  line>