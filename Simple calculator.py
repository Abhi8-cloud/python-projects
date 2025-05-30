def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "not divisible by zero"
    return x/y

print("Simple Calculator")
print ("Select the operations: +,-,*,/")

num1 = float(input("Enter 1st number: "))
operation = input("Enter the operation: ")
num2 = float(input("Enter 2nd number: "))

if operation == "+":
    result = add(num1,num2)
elif operation == "-":
    result = sub(num1,num2)
elif operation == "*":
    result = multiply(num1,num2)
elif operation == "/":
    result = divide(num1,num2)
else:
    result = "invalid operation"

print("result",result)
# done
