#Define temp and receive input
temp = int(0)
temp = int(input('Please enter the current temperature (Enter 999 to end program): '))

#As long as the temperature is not 999, go through loop           
while (temp != 999):
    #Different paths/specifications
    if (temp > 90):
        print('Wear Shorts')
    elif (temp > 70):
        print('Short sleeves are fine')
    elif (temp > 50):
        print('Wear a jacket')
    elif (temp > 32):
        print('Wear a heavy coat')
    else:
        print('Stay inside')
    #Ask for temperature to check whether or not to stay in loop
    temp = int(input('Please enter the current temperature: '))

#End program
print('Have an excellent rest of your day!')
