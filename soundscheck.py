def sounds():
    '''The function checks whether a entered character is a vowel or a consonent'''
    #prompts user for input.
    chara=input("enter a characeter : ")
    if chara==("a" or "e" or "i" or "o" or "u"):
        print("The character is vowel.")
    else:
        print("The character is consonent.")
#Fundtion called for the opeartion
sounds()
