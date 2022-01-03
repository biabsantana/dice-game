''' Roll Dice
1 - Create a loop where users can roll two dices. Show on the screen the number of the dice
2 - Improve the code to allow two players '''

import random
from operator import itemgetter

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
            players = {
                'player_1': roll_dices(),
                'player_2': roll_dices(),
            }

            print('==== RANKING ====')
            print('The first player got ' + str(players['player_1']))
            print('The second player got ' + str(players['player_2']))

        elif menu == 2:
            loop = False
            print('Exiting...')
        else:
            print('This option is not available!')
        
        input('Press anywhere to continue...')

    except ValueError:
        print('Wrong value entered, try again')
        input('Press anywhere to continue...')
        

