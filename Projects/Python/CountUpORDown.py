#broken code
#Hours wasted here: 0.66



choice=str(input('Would you like to count up or down:'))

#Check if input will be in the accepted values
acceptedValues = ['up', 'u', 'high', 'down', 'd', 'low']
if choice not in acceptedValues:
    print('Bad choice!')
    #Check Choice
if choice in["down","d","low"]:
    #Count down
    increment=int(input('Enter increment:'))
    num=int(input('Enter number to be counted down from:'))
    while num>=0:
        print(num)
        num=num-increment
        if num-increment<0:
            print('Number will be negative!')
            print('End with ExitCode Neg1')
            break
    
if choice in ["up",'u','high']:
    #Count up
    increment=int(input('Enter increment:'))
    num=int(input('Enter number to be counted up from:'))
    upperLimit = int(input('Enter upper limit to be counted to:'))
    while num<=upperLimit:
        print(num)
        num=num+increment # Increment num within the while loop
    #Consider that number will be out of range:
        if num+increment>upperLimit:
            print("Number plus increment is out of range!")
            print('Exiting with ExitCode Pos1')
            break
input('Press any key to exit...')
