#Set future integer values to 0
howManyEntered = int(0)
total = int(0)
average = int(0)

#Ask user for number of test scores, store as howMany
howMany = int(input('How many test scores would you like to average: '))

#As long as how many tests the user has entered is less than
#the amount of tests they wish to enter...
#receive a new test score input, add to total, increment amount of tests entered
while (howManyEntered < howMany):
    testScore = int(input('Test Score: '))
    total += testScore
    howManyEntered += 1

#Calculate and print average
average = float(total/howMany)
print('Your average is: '+str(average))
