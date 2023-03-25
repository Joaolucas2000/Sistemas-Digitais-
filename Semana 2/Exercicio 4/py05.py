student = {'name': 'Jonh', 'age': '25', 'courses': ['Math', 'CompSci']}

print(student)
print(student.get('phone', 'Not Found'))
student['phone'] = '555-5555'
student['name'] = 'Jane'

print(student)


age = student.pop('age')
print(student)
print(age)


print(len(student))
print(student.keys())
print(student.values())


for key, values in student.items():
    print(key, values)
