#  Find  outputs
print({10 , 20}  |  {30 , 20})  #  {10 , 20 , 30}  in  any  order
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})  #  {10 : 'Hyd' , 20 : 'Vja' , 30 : 'Cyb'}
#print(range(4) | range(5))  #   Error  becoz  range  objects  can  not  be  concatenated
#print([10 , 20]  |  [30 , 20])   # Error  becoz  lists  can  not  be  concatenated  with  |  operator




'''
1) How  to  concatenate  sets  and  dictionaries ?  ---> With  |  operator  but  not   with  +  operator

2) How  to  concatenate  lists , tuple  and  strings ?  ---> With  +  operator  but  not   with  |  operator

3) What  about  range  objects ?  --->  They  can  never  be  concatenated
'''
