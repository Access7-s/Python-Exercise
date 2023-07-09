'''
Modify your existing function to take an additional parameter: power,
with a default value of False. If a value of True is provided, your
multiplication table should instead apply the top row as powers instead
of multiplying the numbers.
'''

def main():
    # Prompt the user for the size of the table
    size = int(input("Size of the table: "))
    size += 1

    # Print the multiplication table
    multiplication_table(size, True)


def multiplication_table(size, power=False):
    if power == False:
        # Print the top row of numbers
        for top in range(size):
            top = f"{top:02d}"
            print(f"{top:4}", end="")
        print()

        # Get the multiplier
        for i in range(1, size):
            # Print the side column of numbers
            side = f"{i:02d}"
            print(f"{side:4}", end="")

            # Get the multiplicand
            for j in range(1, size):
                # Calculate the product and format it to have leading zeros
                product = f"{i * j:02d}"
                # Print the product and format it to have padding
                print(f"{product:4}", end="")
                
            # Print a new line after a loop
            print()
    else:
       # Print the top row of numbers
        for top in range(size):
            top = f"{top:02d}"
            print(f"{top:4}", end="")
        print()

        # Get the multiplier
        for i in range(1, size):
            # Print the side column of numbers
            side = f"{i:02d}"
            print(f"{side:4}", end="")

            # Get the multiplicand
            for j in range(1, size):
                # Calculate the product and format it to have leading zeros
                product = f"{i ** j:02d}"
                # Print the product and format it to have padding
                print(f"{product:4}", end="")
                
            # Print a new line after a loop
            print()            


if __name__ == "__main__":
    main()
