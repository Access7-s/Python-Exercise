def netamt(mp,dis):
    Netamount=mp-dis
    return Netamount
mpr=int(input("Enter the marked price: "))
damt=int(input("Enter the discount amount: "))
price=netamt(mpr,damt)
print(f"The total price after discount is {price:.2f}")
