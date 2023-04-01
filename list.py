age0frn=[1,2,3,4,5,6,7]
print(age0frn)

programming_language=['python','java','c++']
print(programming_language[0])

num=[1,6,7,69]
print("Before append ",num)
num.append(20)
print("After append ",num)
num.insert(1,10)
print("After inserting 10 in the place 2nd palce",num)

num2=[99,85,77,"me"]
num2.extend(num)
print ("After extending",num2)
num3=num+num2
print (num3)

listA=[1,2,3]
listB=list(listA)
listA.append(5)
print(listA)
print(listB)
listB.append(7)
print(listB)
del listA[2]
print(listA)

