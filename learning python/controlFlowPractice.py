"""
x = 5
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")


for i in range(5):
    print(i)


x = 0
while x < 5:
    print(x)
    x += 1
"""

userInput = int(input("Please enter a number: "))

while userInput >= 0:
    if userInput % 2 == 0:
        print ('Even')
        #userInput = int(input("Please enter a new number: "))
    else:
        print('Odd')
        #userInput = int(input("Please enter a new number: "))

    userInput = int(input("Please enter a new number: "))


print('you entered a negative number, ending program...')

