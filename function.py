def greeting(message):
    print(message)
greeting("This is a greeting")
greeting("Welcome Home")
# Choice Based Program #
def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def division(a,b):
    return a/b
def multiply(a,b):
    return a*b
def powerof(a,b):
    return a**b
print("calculator")
print("Choose any one of the options")
print("1.+")
print("2.-")
print("3./")
print("4.*")
print("5.** This means Power of")
choice = int(input("Enter your Choice:"))
a=int(input("Enter a Number:"))
b=int(input("Enter a Number:"))
if choice==1:
    print("Additon:",add(a,b))
elif choice==2:
    print("Minus",minus(a,b))
elif choice==3:
    print("Division",division(a,b))
elif choice==4:
    print("Multiply",multiply(a,b))
elif choice==5:
    print("Powerof",powerof(a,b))
else:
    print("Decision is Invalid!!")
