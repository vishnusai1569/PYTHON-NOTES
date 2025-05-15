#  Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))   #  Inserts  5  tuples  into  object  pq
pq . put(('Delhi' , 20))
pq . put(('Chennai' , 15))
pq . put(('Pune' , 5))
pq . put(('Mumbai' , 12))
while   not  pq . empty():  # Executed  until  object  pq  is  empty
        print(pq . get())  #  ('Chennai', 15)  <next  line> ('Delhi', 20)  <next  line>  ('Hyd', 10) <next  line> ('Mumbai', 12)  <next  line>  ('Pune', 5)   <next  line>


# Tuples  are  deleted  based  on  1st  element  but  not  on  2nd  element