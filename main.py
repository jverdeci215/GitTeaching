def add(x,y):
    return x+y

def diff(x,y):
    return x-y

def div(x,y):
    return x**y

def mod(x,y):
    return x%y

if __name__ == "__main__":
    num1 = input("Please enter a number: ")
    op = input("Please enter an operation('+';'-';'d'): ")
    num2 = input("Please enter another number: ")
    if(op == "+"): print("The sum is: {}".format(add(int(num1),int(num2))))
    elif(op == "-"): print("The difference is: {}".format(diff(int(num1),int(num2))))
    elif(op == "x"): print("The product is: {}".format(mult(int(num1),int(num2))))
    elif(op == "/"): print("The quotient is: {}".format(div(int(num1),int(num2))))
