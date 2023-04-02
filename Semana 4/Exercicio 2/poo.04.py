#poo4

class Dog:
    
    def bark(self):
        print('bark')
    
    def add_one(self, x):
        return x+1
        
d = Dog()
d.bark()
print(d.add_one(5))

print(type(d)) 
