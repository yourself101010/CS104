"""
Name: Tennessee Tremain
Project: Queue Simulation
Date: 11/18/21
"""

#Define Variables
names = []
name = ''

#Receive 10 names
for i in range(10):
    name = input('Enter name ' + str(i+1) + ': ')
    names.append(name)

#First Way: Iterate through list using for loop (built-in python functionality)
for item in names:
    print(item)
    print()

#Second Way: Using 'pop' list functionality
for i in range(len(names)):
    print(names.pop(0))
    print()
