# Find  outputs  (Home  work)
from  queue  import  Queue
q = Queue()
q . put(('Hyd' , 10))   #  Inserts  5  tuples  into  object  'q'
q . put(('Delhi' , 20))
q . put(('Chennai' , 15))
q . put(('Pune' , 5))
q . put(('Mumbai' , 12))
while   not  q . empty(): #   Executed  until  object  'q'  is  empty
	print(q . get()) #  ('Hyd', 10)  <next  line>  ('Delhi', 20)  <next  line>  ('Chennai', 15)  <next  line>  ('Pune', 5)  <next  line>  ('Mumbai', 12)  <next  line>