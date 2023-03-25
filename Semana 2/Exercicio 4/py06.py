language = 'python'

if language == 'python':
    print('Conditional was True')
elif language == 'Java':
    print('Language is Java')
    
else: 
    print('No match')
    
       
    
user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
    
else: 
    print('Bad Creds')
    
    
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(id(a))
print(id(c))

condition = 0 

if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')
