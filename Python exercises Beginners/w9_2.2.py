def readfile(fname):
    try:
        data=open(fname,"r")
        file=data.read()
        return file
    except:
        print("Error: Input/Output Error")

f_name=input("Filename: ")
print(readfile(f_name))
