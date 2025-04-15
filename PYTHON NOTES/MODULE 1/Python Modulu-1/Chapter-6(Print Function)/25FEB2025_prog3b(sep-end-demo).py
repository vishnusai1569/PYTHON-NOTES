# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')  #   25  <space>  10.8  <space>  Hyd   ---   <same  line>
print(a , b , c , sep = ',,,')   #   25  ,,,  10.8 ,,,  Hyd  <next line>
print(a , b , c , sep = ':::' , end = '\t\t\t')    #   25  :::  10.8  :::  Hyd  <tab><tab><tab>  <same  line>
print(a , b , c)    #   25  <space>  10.8  <space>  Hyd  <next  line>


'''
25 10.8 Hyd---25,,,10.8,,,Hyd
25:::10.8:::Hyd                 25 10.8 Hyd
'''



'''
1) How  many  lines  of  output  is  generated  when  the  program  is  executed ?  --->  2

2) What  does  sep  argument  do ? --->  Determines  the  delimeter  to  be  printed  'between'  the  results
    What  does  end  argument  do ?  --->  Determines  the  delimeter  to  be   printed  at  the  'end'  of  the  line
'''
