a=float(input("enter first number :"))

b = input("enter operators +, -, /,*, :" )

c= float(input("enter second number :"))

if b == "+":
    result= a + c
    print("Result:",result)

elif b == "-" :
    result= a - c
    print("Result:",result)



elif b == "*":
    result= a * c
    print("Result:",result)

elif b == "/":
    if c == 0:
        print("cannot divide by zero")
    else: 
        result= a / c
        print("Result:",result)


else :
    print("invalid oprators")