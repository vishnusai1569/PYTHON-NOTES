try:

    n=int(input('enter the no(1-12) : '))
    if n==1:
        print("jan")
    elif n==2:
        print("feb")
    elif n==3:
        print("march")
    elif n==4:
        print("april")
    elif n==5:
        print("may")
    elif n==6:
        print("june")
    elif n==7:
        print("july")
    elif n==8:
        print("aug")
    elif n==9:
        print("sep")
    elif n==10:
        print("oct")
    elif n==11:
        print("nov")
    elif n==12:
        print("dec")
    elif n!=range(12):
        print("enter a integer from 1 to 12")

except:
    print("input should be integer number")