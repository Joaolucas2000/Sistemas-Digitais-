#Lists

courses = ['History', 'Math', 'Physics', 'CompSci']
courses2 = ['Art', 'Education']


print(courses)
print(courses[0])
print(courses[-1])
print(courses[0:2])
print(courses[2:])

courses.insert(0, 'Art')
print(courses)

courses.insert(0, courses2)
print(courses)
courses.extend(courses2)
print(courses)
courses.append(courses2)
print(courses)

popped = courses.pop()
print(popped)

courses.reverse()
print(courses)


nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)


print(courses.index('Art'))


for index, course in enumerate(courses, start=1):
    print(index, course)
    

#Tuples

tuple1 = ('History', 'Math', 'Physics', 'CompSci')
tuple2 = tuple1

print(tuple1)
print(tuple2)

#tuple1[0] = 'Art' Erro pq tuplas sao imutaveis



#Sets

#Empty Lists
empty_list = []
empty_list = list()
#Empty tuples
empty_tuple = ()
empty_tuple = tuple()
#Empty sets
empty_set = {}
empty_set = set() 
