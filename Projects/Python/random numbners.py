import random

print('Welcome to the RNG generator!')

# Ensure user enters valid numbers
while True:
    try:
        lowNum = int(input('Enter lower limit:'))
        highNum = int(input('Enter upper limit:'))
        
        # Ensure lower limit is less than upper limit
        if lowNum >= highNum:
            print("The lower limit must be less than the upper limit. Please try again.")
        else:
            break
    except ValueError:
        print("Please enter valid integers.")


randomNum = random.randint(lowNum, highNum)
print('Your random number is', randomNum, '!')


input('Press Enter to exit...')
