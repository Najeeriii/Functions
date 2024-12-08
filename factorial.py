def recurfactorial(n):
    if n==1:
        return n
    else:
        return n*recurfactorial(n-1)
        
num = int(input("Enter a Number"))

if num<0:
    print("Sorry, factorial does not exist for negative numbers")
elif num== 0:
    print("The Factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recurfactorial(num))