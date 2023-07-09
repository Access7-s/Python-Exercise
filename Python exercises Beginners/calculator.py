def add(a,b):
    '''it adds up two given numbers'''
    return a+b
def sub(a,b):
    '''it substracts two given numbers'''
    return a-b
def multiply(a,b):
    '''it multiplies two given numbers'''
    return a*b
def divide(a,b):
    '''it divides two given numbers'''
    return a/b
def modulus(a,b):
    '''it shows the remiender of two numbers when used while division'''
    return a%b
def exponential(a,b):
    '''It raises the second value to the power of the first value entered'''
    return a**b

a=int(input("enter first number:"))
b=int(input("enter next number:"))
help(add)
addition=add(a,b)
print(f"Sum: {addition}")
help(sub)
subtract=sub(a,b)
print(f" Substraction: {subtract}")
help(multiply)
product= multiply(a,b)
print(f"Multiplication: {product}")
help(divide)
division=divide(a,b)
print(f"Division: {division}")
help(modulus)
rem=modulus(a,b)
print(f" Modulus : {rem}")
help(exponential)
exponent=exponential(a,b)
print(f" Exponential value :{exponent}")
