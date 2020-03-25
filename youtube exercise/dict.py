student= {'name': 'John', 'age': 25, 'course': ['Math', 'CompSci']}

print(student)
print(student['name'])
print(student['course'])
print(student.get('name'))
print(student.get('phone', 'Not Found')) #for keys not exist, turn out 'Not Found'

student['phone'] = '555-5555'
student['name'] = 'Jane'

student.update({'country': 'USA'})

del student['age'] #delete
phone = student.pop('phone')
print(phone)
print(student)


print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)

for key in student:
    print(key)

for value in student.values():
    print(value)
