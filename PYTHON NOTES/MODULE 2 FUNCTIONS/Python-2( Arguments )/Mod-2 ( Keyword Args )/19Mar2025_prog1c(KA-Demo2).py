# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)



'''
Emp  Number :   25        Emp  Name : Rama Rao            Salary : 10000.0
Emp  Number :   35        Emp  Name : Sita                Salary : 20000.0
Emp  Number : Rama  Rao           Emp  Name :         30000.0     Salary : 20
'''

'''
1) What  does  {empno:4)  indicate ? ---> empno  in  a  width  of  4  characters  with  leading  spaces
    How  is  25  printed ?  ---> <2  spaces>25

2) What  does  {ename:15}  indicate ? ---> ename  in  a  width  of  15  characters  with  trialing  spaces
     How  is  "Rama  Rao"  printed ?  ---> Rama  Rao<7  spaces>

3) What  does  {ename:^15}  indicate ? --->  ename  in  a  width  of  15  characters  with  center  alignment
     How  is  "Rama  Rao"  printed  ? --->  <3  spaces>Rama Rao<4  spaces>

4) What  is  the  advantage  of  width  specification  ?  ---> Results  are  aligned

5) What  is  the  dis-advantage  of  PA's ?  --->  Incorrect  results  when  arguments  are  passed  in  a  different  order

6) What  is  the  advantage  of  KA's ?  --->  Perfect  results  even  though  arguments  are  passed  in  a  different  order
'''
