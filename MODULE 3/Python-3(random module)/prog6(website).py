
'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  --->  Opens  google.com  website

2) Where  is  open()  function  defined  ?  --->  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''
from  random  import  *
import  webbrowser
import    time
list = ['google.com' , 'youtube.com' , 'gmail.com' , 'rediff.com' , 'amazon.com' , 'bing.com' ,  'flipkart.com' ]
while   True:
	site = choice(list)
	webbrowser . open(F'http://{site}')
	sec = randint(5 , 20)
	time . sleep(sec)
