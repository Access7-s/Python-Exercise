'''a Python program that prompts the user for a list of integers and
stores them in a list. For all values that are greater than 100,
the string 'over' should be stored instead. The program should
display the resulting list.'''
#creating an empty list to store values
listA = []
#prompting user for input
add = input("Enter numbers to be added to the list : ")
while add != "":
    if int(add) < 100 :
        listA.append(add)
    elif int(add) > 100 :
        listA.append("over")

    add=input("Enter another number to be added: ")
print (listA)
