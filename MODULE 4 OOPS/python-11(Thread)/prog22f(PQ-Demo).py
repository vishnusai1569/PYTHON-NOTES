#  Find  outputs  (Home  work)
from   queue   import  PriorityQueue
import  random
pq = PriorityQueue()
for  i  in  range(1 , 6):
	pq . put(random . randint(1 , 100)) #  Inserts  5  random  numbers  into  object  pq
print('Deleted  elements')
while  not   pq . empty():  #   Execute  until  object   pq   is  empty
        print(pq . get())  #  Numbers  in  ascending  order
print(pq . get())  # main  thread  waits  until  an  element  is  inserted  into  object  pq
print('End') #  Not  executed