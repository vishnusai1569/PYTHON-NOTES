#  Find  outputs (Home  work)
import  re
string  =  'z7.Q-$2 b[9.a%6$G&k.%'
print(re . findall ('[a-z]'  ,  string)) #  List  of  all  lowercase  alphabets  i.e.  ['z', 'b', 'a', 'k']
print()
print(re . findall ('[0-9]'  ,  string)) #   List  of  all  digits  i.e. ['7', '2', '9', '6']
print()
print(re . findall ('[^A-Za-z0-9]'  ,  string)) #   List  of  all   special  chars  i.e. ['.', '-', '$', ' ', '[', '.', '%', '$', '&', '.', '%']
print()
print(re . findall ('.'  ,  string)) #   List  of  all  the  characters  i.e.  ['z', '7', '.', 'Q', '-', '$', '2', ' ', 'b', '[', '9', '.', 'a', '%', '6', '$', 'G', '&', 'k', '.', '%']
print()
print(re . findall ('[.]'  ,  string)) #   List  of  all  dots  i.e.  ['.', '.', '.']
print()
print(re . findall ('[$]'  ,  string)) #   List  of  all  $'s  i.e.  ['$', '$']
print()
print(re . findall ('[%]'  ,  string)) #   List  of  all  %'s  i.e.  ['%', '%']
print()
print(re . findall ('[az-]'  ,  string)) #   List of  all  'a' , 'z'  and   '-'  i.e.  ['z', '-', 'a']