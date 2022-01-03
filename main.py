''' Roll Dice
1 - Create a loop where users can roll two dices. Show on the screen the number of the dice '''

import random

def roll_dices():
    first_dice = [random.randint(1,6)]
    second_dice = [random.randint(1,6)]
    return first_dice + second_dice

loop = True
while loop:
    print('---------- DICE ROLLER ----------')
    print('Welcome!')
    print('1 - Roll a dice')
    print('2 - Exit')
    
    try:
        menu = int(input('Choose an option: '))
        if menu == 1:
            print('Rolling dices...')
            print('The result was '+ str(roll_dices()))
        elif menu == 2:
            loop = False
            print('Exiting...')
        else:
            print('This option is not available!')
        
        input('Press anywhere to continue...')

    except ValueError:
        print('Wrong value entered, try again')
        input('Press anywhere to continue...')
        

