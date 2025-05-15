# Find  outputs (Home  work)
import   time
list = [
             {
                'Roll Num' :  10 ,
                'Stud Name' : 'Rama Rao' ,
                'Marks' : 75
              } ,
              {
                'Roll Num' :  20 ,
                'Stud Name' : 'Sita' ,
                'Marks' : 52
              } ,
             {
               'Roll Num'  :  15 ,
               'Stud Name' : 'Kiran' ,
               'Marks' : 65
             } ,
             {
               'Roll Num'  :  18 ,
               'Stud Name' : 'Amar' ,
               'Marks' : 48
             } ,
             {
               'Roll Num' :  5 ,
               'Stud Name' : 'Rajesh' ,
               'Marks' : 82
             }
        ]  #  List  of  dictionaries
f = filter(lambda  x :  x['Marks'] >= 60 , list) #  Creates  an  empty  filter  object
while   True:
	try:
		print(next(f))  #   Those  dictionaries  where  value  of   marks  is  >= 60
		time . sleep(1)
	except:
		break

'''
{ 'Roll Num' :  10 , 'Stud Name' : 'Rama Rao' ,'Marks' : 75}
{'Roll Num'  :  15 , 'Stud Name' : 'Kiran' , 'Marks' : 65}
{'Roll Num' :  5 , 'Stud Name' : 'Rajesh' , 'Marks' : 82}
'''

'''
1) What  is  'x'  in  the  lambda  function ?  --->  Each  dictionary  of  the  list

2) What  is  x['Marks']  in  the  lambda  function ?  ---> Value  of  Marks  in   dictionary  'x'

3) How  many  times  is  lambda  function  executed ?  --->  5  times  becoz  there  are  five  dictionaries  in  the  list

4) How  many  times  is  while  loop  executed ?  --->  3 + 1 = 4  times

5) How  to  define  regular  function  instead  of  lambda  function ?  --->  def  f1(x):
																														  return  x['Marks']  >= 60

6) How  to  create  filter  object  with  regular  function ? ---> f = filter(f1 , list)
'''