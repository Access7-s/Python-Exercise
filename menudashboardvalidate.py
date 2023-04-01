validate = False
while not validate:
    print("choices")

    which = int(input("Enter a selection"))
    if (which == 1 or which == 2 or which == 3):
        validate = True
    else:
        print("invalid input")
