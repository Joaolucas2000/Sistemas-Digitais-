li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li)

print('Sorted Variable:', s_li)
li.sort(reverse=True)
print('Original Variable:', li)


tup = (9, 1, 8, 2, 7, 3)
#tup.sort() Da erro pq tuple nao pode ser alterada

di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'MAc'}

s_di = sorted(di)
print('dict', s_di)


li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li)
print(li)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self):
        return 'return'
    
e1 = Employee('Carl', 37, 7000)
e1 = Employee('Carl', 29, 8000)
e1 = Employee('John', 37, 7000)
