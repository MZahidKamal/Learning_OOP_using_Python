#-----------------------------------------------------------------------------------------------------------------------
# 3.4 Dictionary and Dictionary methods in python
#-----------------------------------------------------------------------------------------------------------------------
# Dictionary items are ordered, changeable, and does not allow duplicates.
# x = {"name" : "John", "age" : 36}

person_info = {'Name': 'Robert Bosch', 'Address': 'Frankfurt', 'Age': 25, 'Profession': 'Engineer', 'Hobby': 'Drawing'}

print(person_info)
print()

print(person_info.keys())
print(person_info.values())
print()

for key, value in person_info.items():
    print(f'{key}: {value}')
print()
#-----------------------------------------------------------------------------------------------------------------------
# Adding new item (key and value) in a dictionary.
person_info['Language'] = 'English'

for key, value in person_info.items():
    print(f'{key}: {value}')
print()
#-----------------------------------------------------------------------------------------------------------------------
# Modifying an item (key and value) in a dictionary.
person_info['Hobby'] = 'Swimming'

for key, value in person_info.items():
    print(f'{key}: {value}')
print()
#-----------------------------------------------------------------------------------------------------------------------
# Deleting an item (key and value) from a dictionary.
del person_info['Hobby']

for key, value in person_info.items():
    print(f'{key}: {value}')
print()
#-----------------------------------------------------------------------------------------------------------------------
person_info_list = list(person_info)
print(person_info_list)
print(type(person_info_list))
#-----------------------------------------------------------------------------------------------------------------------
