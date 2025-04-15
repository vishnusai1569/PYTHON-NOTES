import sys

argv = sys.argv

if len(argv) == 1:
    print("Pls send inputs")
else:
    a = []
    contains_string = False
    contains_number = False

    for arg in argv[1:]:
        try:
            num = float(arg)  # Convert to float if possible
            a.append(num)
            contains_number = True
        except ValueError:
            contains_string = True

    if contains_number and contains_string:
        print("Inputs can not be number and string")
    else:
        if contains_string:
            print("What is the largest command line input ? --->", max(argv[1:]))
        else:
            print("What is the largest command line input ? --->", max(a))

