# Find  outputs
list = [10 , 20 , 15 , 18]
print(list)  #  [10,20,15,18]
list . insert(-2 , 25)  #  Inserts  25  after  index  -2  of  the  list
print(list) #  [10 , 20 , 25 , 15 , 18]
list . insert(-len(list) , 12)  #  How  to  insert  12  at  the  begining  of  list  with  -ve  index
print(list)   #  [12 , 10 , 20 , 25 , 15 , 18]
list . insert(-10 , 19)  #  Inserts   19  at  the  begining  of  list  becoz  -10  is  invalid  index
print(list)   #  [19 , 12 , 10 , 20 , 25 , 15 , 18]
#How  to  insert  19  at  the  end  of  list  with  -ve  index  --->  Not  possible





'''
insert()  method
--------------------
1) What  does  insert()  method  do ?  --->  Inserts   an  element  at  the  specified  index  of  the  list

2) What  are  the  two  arguments  of  insert()  method ?  --->  Index  and  element  to  be  inserted

3) list . insert(4 , element)
    Where  is  the  element  inserted   if  4  is  a  valid  index  ?  --->  At  index  4

4) list . insert(-4 , element)
    Where  is  the  element  inserted   if  -4  is  a  valid  index  ?  ---> After  index  -4

5) list . insert(Invalid  +ve  index , element)
    Where  is  the  element  inserted  ?  ---> At  the  end  of  the  list

6) list . insert(Invalid  -ve  index , element)
    Where  is  the  element  inserted  ?  ---> At  the  begining  of  the  list

7) How  to  insert  an  element  at  the  end  of  the  list  with  valid  +ve  index ?  --->  list . insert(len(list) , element)
    How  to  insert  element  at  the  begining  of  the  list  with  valid  +ve  index  ?  ---> list . insert(0 , element)

8) How  to  insert  element  at  the  begining  of  the  list  with  valid  -ve  index ?  --->  list . insert(-len(list) , element)
     How  to  insert  element  at  the  end  of  the  list  with  -ve  index ?  --->  Not  possible

9) What  is  the  difference  between  append()  and  insert()  methods  ?  --->
														append()  method  inserts  element  at  the  end  of  the  list  but
														insert()  method  can  insert  element  any  where  in  the  list
'''
