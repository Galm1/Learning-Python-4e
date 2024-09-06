
file = open("my_data.txt", "w")
file.write('Hello world!\n')
file.write('This should be a new line.')

with open('my_data.txt', 'r') as file:
    content = file.read()
    print(content)

file = open('my_data.txt', 'a')
file.write("\nThis should be at end post append")
file.close()

with open('my_data.txt', 'r') as file:
    content = file.read()
    print(content)


with open('my_data.txt', 'r') as file:
    for line in file:
        print(line.strip())

try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('The file does not exist')


import os

if os.path.exists('my_data.txt'):
    os.remove('my_data.txt')
else:
    print('The file cannot be deleted because it does not exist.')

