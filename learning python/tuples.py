#tuples are like lists but immutable, lets mess around with them a bit
T = (1,2,3,4)
print(T)
print('Printing the length of tuple T. Should be 4...')
print(len(T))

T + (5,6)
print('added via concatenation 5 and 6. Printing...')
print(T)

print('indexing and count:...')
print(T[0])
print(T.index(4))
print(T.count(4))
