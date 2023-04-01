def diff(n):
    if n>17:
        sub=(n-17)*2
    else:
        sub=n-17
    return sub
num=int(input("Enter a number: "))
difference=diff(num)
print("The required result is",difference)
