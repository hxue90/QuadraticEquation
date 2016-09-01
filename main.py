def askA():
    return(int(input("What is the value of A ")))

def askB():
    return (int(input("What is the value of B ")))

def askC():
    return (int(input("What is the value of C ")))

def askX():
    return (int(input("What is the value of X ")))

def printQ(a, b, c, x):
    quad = (a * (x ** 2)) + (b * x) + c
    if b >= 0:
        print("The following quadratic was entered: %sX^2+%sX+%s" % (a, b, c))
    else:
        print("The following quadratic was entered: %sX^2%sX+%s" % (a, b, c))
    print("The value of the quadratic is %s" % quad)

def main():
    print("Welcome to the Program! Please enter the value of A, B, C and X at the corresponding prompts")

    a = askA()
    b = askB()
    c = askC()
    x = askX()

    printQ(a, b, c, x)



if __name__ == "__main__":
    main()