#  How  to  print  outputs  in  colors
import   os , time
os . system('color   4')  #  Modifies  text  color  to  4   i.e.  red
print('Hyd')  #  Prints  'Hyd'  in  red  color
time . sleep(5)
os . system('color  2')   #  Modifies  text  color  to  2   i.e.   green
print('Sec')   #  Prints  'Sec'  in   green  color  and  'Hyd'  is  also  modified  to   green  color
time . sleep(5)
os . system('color  6')   #  Modifies  text  color  to  6   i.e.   Yellow
print('Cyb')   #  Prints  'Cyb'  in   yellow  color  and    also  modifies  'Hyd'   and  'Sec'  to   yellow  color


'''
What  does  color  command  do ?  --->  Changes  text  color

0 = Black
1 = Blue
2 = Green
3 = Aqua
4 = Red
5 = Purple
6 = Yellow
7 = White
8 = Gray
9 = Light Blue
A = Light Green
B = Light Aqua
C = Light Red
D = Light Purple
E = Light Yellow
F = Bright White
'''