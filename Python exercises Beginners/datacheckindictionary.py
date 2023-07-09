def dataindict(key,value):

    student_data = [  {"student_id": 1, "name": "Jean Castro", "class": "V"},
                    {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
                    {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
                    {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
                    {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
    valid= False
    for i in student_data:
        if key in i:
            if value in i[key]:
                valid = True
    if valid== True:
        print (f"key: '{key}' and Value: '{value}' do exist")
    else:
        print (f"key: '{key}' and Value: '{value}' donot exist")

key= input("Enter the key: ")
value= input ("enter the value : ")
dataindict(key,value)
