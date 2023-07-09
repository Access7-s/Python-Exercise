def vowelist(listall):
    listvwl=[]
    for i in listall:
        if (i[0]) in ['a','e','i','o','u']:
            listvwl.append(i)
    return listvwl
listall=['apple','ball','cat','egg','Shubham']
print(vowelist(listall))
