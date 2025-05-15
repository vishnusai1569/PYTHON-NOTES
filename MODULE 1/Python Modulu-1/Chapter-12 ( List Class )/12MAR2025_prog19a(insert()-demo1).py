# insert()  method  demo  program
list = [10 , 20 , 15 , 18]
print(list)  #  [10,20,15,18]
list . insert(2 , 25)# Inserts  25  at  index  2  of  the  list
print(list)  # [10,20,25,15,18]
list . insert(len(list) , 12) #  How  to  insert  12  at  the  end  of  list
print(list) #  [10,20,25,15,18,12]
list . insert(0 , 19)  #  How  to  insert  19  at  the  begining  of  list
print(list)  #   [19,10,20,25,15,18,12]
list . insert(10 , 14)  #  Inserts  14  at   the  end  of list  becoz  10 is  invalid  index
print(list)  #   [19,10,20,25,15,18,12,14]
