''' Roll Dice
1 - Create a loop where users can roll two dices. Show on the screen the number of the dice
2 - Improve the code to allow two players
3 - Let the user decide how many players and show a ranking at the end '''

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

            num_players = int(input('How many players? '))
            print('Rolling dices...')

            totalScore = dict()
            for i in range(0, num_players):
                move = roll_dices()
                print('Player ', i+1 , 'got: ', move)
                sumScore = {'Player '+str(i+1): sum(move)}
                totalScore.update(sumScore)

            print('')
            print('==== RANKING ====')
            ranking = sorted(totalScore.items(), key=lambda x: x[1], reverse=True)
            print(ranking)

        elif menu == 2:
            loop = False
            print('Exiting...')
        else:
            print('This option is not available!')
        
        input('Press anywhere to continue...')

    except ValueError:
        print('Wrong value entered, try again')
        input('Press anywhere to continue...')
        

