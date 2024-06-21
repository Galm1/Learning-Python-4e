x = input("Type something: ")
print("your entry: ", x)

x= input("enter your name: ")
y= input("enter your age: ")
z=input("enter your gender: ")

print("Your name: ", x, "\nYour age: ", y, "\nYour gender: ", z)

'''person = {
    'name' : x,
    'age' : y,
    'gender' : z
    }'''

people = {
    'person1' : {
        'name' : x,
        'age' : y,
        'gender' : z
        }
    }

print(people['person1']['name'])

'''print(person['name'])'''

for person, details in people.items():
    print(f'{person}:')
    for key, value in details.items():
        print(f'   {key}: {value}')
