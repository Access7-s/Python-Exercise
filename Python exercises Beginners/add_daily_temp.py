def add_daily_temp(tempdict,temp,day):
    if day not in tempdict:
        tempdict[day]=temp

    return tempdict
tempdict1={"Sunday": 20, "Tuesday":25, "Thursday": 40, "Saturday": 35}
tempdictn=add_daily_temp(tempdict1, 22, 'Monday' )
print(tempdictn)
tempdictn1=add_daily_temp(tempdict1, 55, "Saturday")
print(tempdictn)

    
