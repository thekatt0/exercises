#start
x = 'Y'

while x.upper() == 'Y':
    x = input('Would you like to play? Insert Y/N ')
    if x.upper() == 'N':
        continue
    p1 = input('Player 1; Rock, Paper or Scissors? ')
    p2 = input('Player 2; Rock, Paper or Scissors? ')



#comparisons
#player 1 wins
    if((p1.upper() == 'PAPER' and p2.upper() == 'ROCK') or (p1.upper() == 'SCISSORS' and p2.upper() == 'PAPER') or (p1.upper() == 'ROCK' and p2.upper() == 'SCISSORS')):
        print('Player 1 wins! ')

#tied
    elif ((p1.upper() == 'ROCK' and p2.upper() == 'ROCK') or (p1.upper() == 'PAPER' and p2.upper() == 'PAPER') or (p1.upper() == 'SCISSORS' and p2.upper() == 'SCISSORS')):
        print('Its a tie ')

#player 2 wins
    elif((p2.upper() == 'PAPER' and p1.upper() == 'ROCK') or (p2.upper() == 'SCISSORS' and p1.upper() == 'PAPER') or (p2.upper() == 'ROCK' and p1.upper() == 'SCISSORS')):
        print('Player 2 wins! ')

else:
    print('Goodbye! ')






        