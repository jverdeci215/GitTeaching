def add(x,y):
    return x+y

def diff(x,y):
    return x-y

def mult(x,y):
    return x*y

if __name__ == "__main__":
    num1 = input("Please Enter A Number: ")
    num2 = input("Please Enter Another Number: ")
    op = input("Please enter an operation(add/diff/mult): ")
    if(op == "add"): print("The sum is: {}".format(add(int(num1),int(num2))))
    elif(op == "diff"): print("The difference is: {}".format(diff(int(num1),int(num2))))
    elif(op == "mult"): print("The product is: {}".format(mult(int(num1),int(num2))))
