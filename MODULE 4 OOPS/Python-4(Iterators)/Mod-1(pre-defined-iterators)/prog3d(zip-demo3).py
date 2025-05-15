#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):  #   Creates  an  empty  zip  object  which  is  iterated  on fly
	print(x) #  Each  tuple  yielded  by  zip  iterator
	time . sleep(1)

'''
('Telangana' , 'Hyderabad' , 50000000)
('Andhra  Pradesh' , 'Amaravathi' , 40000000)
('Karnataka' , 'Banglore' , 70000000)
('TamilNadu' , 'Chennai' , 60000000)
('Maharastra' , 'Mumbai'' , 30000000)
'''


'''
1) How  many  sequences  can  be  zipped ? --->  0 , 1  (or)  more  than  one

2) How  many  times  is  for  loop  executed ?  ---> 5  times
'''