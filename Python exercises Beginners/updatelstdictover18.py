def updatedict(lstdict1):
    lstdict2=[]
    for i in lstdict1:
        for key in i:
            if (i[key] > 18):
                lstdict2.append(i)

    return lstdict2
lstdict1= [
            {"Shubham": 18},
            {"Saunak": 17},
            {'Rickey': 22},
            {"Rewant":30},
            ]
print(updatedict(lstdict1))
