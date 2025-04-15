import sys
try:
    a=sys.argv[1:]
    c=[]
    for i in a:

        c.append(i)
    print(max(c))
except (TypeError,ValueError):
    print("INput can not be number and string")