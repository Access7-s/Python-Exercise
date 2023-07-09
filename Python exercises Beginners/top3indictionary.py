item_rating={'item1': 45.50, 'item2': 35, 'item3': 41.55, "item4": 55, 'item5': 24}
data=sorted(item_rating,key=item_rating.get, reverse= True)

for i in range(3):
    print(f"{data[i]}: {item_rating[data[i]]}")
