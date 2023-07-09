def sum(no):
    if (no == 1):
        return 1
    else:
        return (no + sum(no-1))
print(sum(3))
