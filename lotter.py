#Mayk Rambeau
# using Python 3.5.2

import random, os
x = 0

print ("Welcome to lottery numbers, random numbers generated " + '\n')
trynow = input("do you want to generate numbers (yes/no)  "+ '\n')
trynow.lower()

while trynow == "yes":
    for x in range(6):
    # while x < 6:
        lotterynumbers = []
        lotterynumbers.append(random.randint(1, 99))
        x += 1
        lotterynumbers.sort()
        print(lotterynumbers)
    clear = "\n" * 100
    trynow = input('generate new numbers: try again? (yes/no) ')
    print(clear)
else:
    print('bye')

