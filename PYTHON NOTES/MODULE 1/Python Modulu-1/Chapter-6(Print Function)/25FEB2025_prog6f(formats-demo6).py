#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))  #    25    10.927400    Hyd
print('%i    %g    %s'    %(a , b , c))   #    25    10.9274    Hyd
print('%s    %s    %s'  %(a , b , c))   #    25    10.9274    Hyd
print('%d    %g    %s'  , a , b , c)    #  %d   %g   %s  <space>  25  <space>  10.9274   <space>  Hyd
#print('%d    %g      %s'   a , b , c)  #  Error  becoz   %  is  missing  for  objects  a , b  and  c
#print('%d    %g    %s'  ,  %(a , b , c))  #  Error  due  to  comma
#print('%d    %g    %s'    %a%b%c)  #  Error  due  to  multiple  %'s
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)  #    25  <space>  10.927400  <space>  Hyd
