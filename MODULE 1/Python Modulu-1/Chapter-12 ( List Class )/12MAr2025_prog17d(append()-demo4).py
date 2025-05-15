#  Find  outputs
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . append(b)  #  Appends  list  'b'  to  list  'a'
print(a)  # [10,20,30,40,[50,60,70]]
print(len(a))  #  5
print(a[4]) #  How  to  print  inner  list  --->  [50,60,70]
print(a[4][0])  #  How  to  print  50  --->  [50,60,70][0]  is  50
print(a[4][1])  #  How  to  print  60  --->  [50,60,70][1]  is  60
print(a[4][2]) #  How  to  print  70   --->  [50,60,70][2]  is   70


'''
append()   method
---------------------
1) What  does  append(x)  do ?  --->  Inserts   'x'  at  the  end  of  the  list

2) What  is  the  argument  of  append()  method  ?  ---> Any  Pyhton  object
																						 i.e.  sequence  (or)  non-sequence

3) list . append(sequence)
    What  is  appended  to  the  list  ? ---> Sequence  itself  but  not  the  elements  of  sequence
'''
