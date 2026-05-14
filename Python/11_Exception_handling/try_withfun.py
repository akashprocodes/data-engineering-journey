
# Try exception with function

def myfun(x):

    try:
        if x % 2 == 0:
            print ("Even number")

    except:
        print("Something went wrong")

myfun(10)