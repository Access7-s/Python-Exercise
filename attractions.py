def attra():'''This function provides the information on the attraction places of four cities'''
    #displays the message to the user
    print("Enter the city name for its tourist attraction.Among Kathmandu, Pokhara, Nepalgunj and Birgunj")
    #asks for input and evaluate the output if condition satisfies.
    cty=input("YOUR desired city: ")
    if cty=="Kathmandu":
        print("Pashupatinath Temple")
    elif cty=="Pokhara":
        print("Fewa Lake")
    elif cty=="Nepalgunj":
        print("Bageshwori Temple")
    elif cty=="Birgunj":
        print("Birgunj Ghanta Ghar")

attra()
