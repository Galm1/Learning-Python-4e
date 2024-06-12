squares = [x ** 2 for x in [1,2,3,4,5]]
print('comprehension expression:')
print(squares)

#now using for loop
squares = []
for x in [1,2,3,4,5]:
    squares.append(x**2)

print('\nusing for loop now:')
print(squares)

print('above should give same result')
