def add(x,y):
    return x+y

def diff(x,y):
    return x-y

if __name__ == "__main__":
    num1 = input("Please Enter A Number: ")
    num2 = input("Please Enter Another Number: ")
    print("The sum is: {}".format(add(int(num1),int(num2))))
