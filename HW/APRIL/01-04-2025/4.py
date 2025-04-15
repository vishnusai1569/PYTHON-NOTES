'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''

def f1(text):
    for word in text.split():
        yield word
t = "This is a sample sentence"
g=f1(t)
for word in g:
    print(word)