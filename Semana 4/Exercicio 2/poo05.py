
#poo5

class Dog:
    def __init__(self, name):
        self.name = name
        print(name)
    def bark(self):
        print('bark')
    
    def add_one(self, x):
        return x+1
        
d = Dog('Tim')
d2 = Dog('Bill') 
