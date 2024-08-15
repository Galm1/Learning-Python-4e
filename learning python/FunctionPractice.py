'''
def greet():
    print('Hello, world!')

greet()
'''

'''
def greet(name):
    print(f'Hello, {name}!')

greet('Alice')
greet('Bob')
'''

'''
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
'''

'''
def greet():
    message = 'Hello!'
    print(message)

greet()

#print(message)  <--- this outside the function gives error because it is out of the functions scope where message is declared
'''

def calculateArea(length, width):
    return length * width

area1 = calculateArea(5, 10)
print(f'The area of the rectangle is: {area1}')

area2 = calculateArea(7, 3)
print(f'The are of the rectangle is: {area2}')

