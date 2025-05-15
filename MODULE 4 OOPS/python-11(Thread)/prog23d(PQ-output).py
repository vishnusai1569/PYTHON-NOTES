# Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10)) #  Inserts  5  tuples  into  object  pq
pq . put(('Hyd' , 20))
pq . put(('Hyd' , 15))
pq . put(('Hyd' , 5))
pq . put(('Hyd' , 12))
print('Deleted tuples')
while   not   pq . empty():  # Executed  until  object pq  is  empty
        print(pq . get())  #  ('Hyd', 5) <next  line>  ('Hyd', 10)   <next  line>  ('Hyd', 12)  <next  line> ('Hyd', 15)  <next  line>  ('Hyd', 20)  <next  line>

# Since  1st  element  is  same  in  all  the  tuples,  deletion  is  made  based  on  2nd  element