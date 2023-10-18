import sys

def add(x,y):
    return x+y

def diff(x,y):
    return x-y

def mult (x,y):
    return x*y

def div(x,y):
    return x/y

def mod(x,y):
    return x%y

if __name__ == "__main__":
    num1 = sys.argv[1]
    op = sys.argv[2]
    num2 = sys.argv[3]
    if(op == "+"): print("The sum is: {}".format(add(int(num1),int(num2))))
    elif(op == "-"): print("The difference is: {}".format(diff(int(num1),int(num2))))
    elif(op == "x"): print("The product is: {}".format(mult(int(num1),int(num2))))
    elif(op == "/"): print("The quotient is: {}".format(div(int(num1),int(num2))))
