#By Shubhankar
import random
import time
print('Welcome to Rock Paper Scissors!')
yn = input('Would you like to play a game?: (Y/N)')
yn = yn.lower().capitalize() #Format user's choice
acceptableValues = ['Yes','Y'] #Check if user says Yes, otherwise No is carried
if (yn not in acceptableValues):
    print('Well, see you soon!') #End of execution, run again
aiChoices = ['Rock','Paper','Scissors']
userChoices = ['R', 'P', 'S','Rock','Paper','Scissors', 'Scissor']
aiChoice = random.choice(aiChoices)
if (yn in acceptableValues):
    print('OK lets start!')
    time.sleep(1)
    userChoice = input('Enter a choice!: ')
    userChoice = userChoice.lower().capitalize()
if(userChoice in userChoices):
    if (userChoice == 'Rock' or userChoice =='R'):
        if (aiChoice == 'Scissors'):
            time.sleep(0.5)
            print('Computer chose ',aiChoice,' you chose Rock, you Win!!')
        if (aiChoice == 'Rock'):
            time.sleep(0.5)
            print('Rock... Paper... Scissors!')
            print('You both chose Rock! Its a tie!!')
            
    if (userChoice == 'Scissors' or userChoice== 'S' or userChoice== 'Scissor'):
        if (aiChoice == 'Paper'):
            time.sleep(0.5)
            print('Rock... Paper... Scissors!')
            print('Computer chose ',aiChoice,'& you chose Scissors! You Win!!')
        if (aiChoice == 'Rock'):
            time.sleep(0.5)
            print('Rock... Paper... Scissors!')
            print('Computer chose ',aiChoice,'& you chose Scissors! You Lost!!')
        if (aiChoice == 'Scissors'):
            time.sleep(0.5)
            print('Rock... Paper... Scissors!')
            print('You both chose Scissors! Its a tie!!')
    if (userChoice == 'Paper' or userChoice == 'P'):
        if (aiChoice == 'Rock'):
            time.sleep(0.5)
            print('Rock... Paper... Scissors!')
            print('Computer chose ',aiChoice,'& you chose Paper! You Win!!')
        if (aiChoice == 'Scissors'):
            time.sleep(0.5)
            print('Rock... Paper... Scissors!')
            print('Computer chose ',aiChoice,'& you chose Paper! You Lost!!')
        if (aiChoice == 'Paper'):
            time.sleep(0.5)
            print('Rock... Paper... Scissors!')
            print('You both chose Paper! Its a tie!!')
            #End of execution
if(userChoice not in userChoices):
    print('Bad Choice! EX Code 0!')



