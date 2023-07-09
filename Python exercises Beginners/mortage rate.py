def mortgage_rate(amount, rate, term):
    total  = amount * (1+ (rate/100) * term)
    print(('${0:.2f} at {1:.2f}% over {2:} years is ${3:.2f}'.format(amount)))
print(mortgage_rate(1000,5,2))
