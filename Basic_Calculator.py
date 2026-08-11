print("MATHMATICAL CALCULATOR")
a=int(input(("Enter first number: ")))
o=input("Enter the operator(+,-,*,%,/,//): ")
b=int(input(("Enter second number: ")))
if o=="+":
    print("Addition of two numbers=",a+b)
elif o=="-":
    print("Substraction of two numbers=",a-b) 
elif o=="*":
    print("Multiplication of two numbers=",a*b) 
elif o=="/":
    print("Division of two numbers=",a//b) 
elif o=="%":
    print("Moduls of two numbers(Remender)=",a%b) 
elif o=="//":
    print("Fractional division of two numbers=",a//b) 
else:
    print("Invalid operation ! Please Enter operation from : +,-,*,/,% and //")    

'''print("Basic arithmetic operations")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
add=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b
sqr=a**2
power=a**b
print("Addition  a and b=",add)
print("Substraction  a and b=",sub)
print("Multiplication  a and b=",mul)
print("Division  a and b=",div)
print("Modulus of a and b=",mod)
print("a to the power b =",power)'''