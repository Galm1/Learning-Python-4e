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
