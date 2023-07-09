def game(zombie):
    if zombie=="straight":
        res=print("Zombie fell in pithole; you lost")
    elif zombie== "left":
        res=print("Zombie lost in jungle and died; you lost")
    else zombie=="right":
        res=print("Zombie found humans his food; you won ")
        return res

zom=input("Enter your choice(in lower case) right or left or straight for zombie to move : ")
game(zom)



    
     

        
    
