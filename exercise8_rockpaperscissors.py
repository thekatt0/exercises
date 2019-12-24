p1 = input('Player 1; Rock, Paper or Scissors? ')
p2 = input('Player 2; Rock, Paper or Scissors? ')

#compare



if ((p1.upper() == 'PAPER' and p2.upper() == 'ROCK') or (p1.upper() == 'SCISSORS' and p2.upper() == 'PAPER') or (p1.upper() == 'ROCK' and p2.upper() == 'SCISSORS')):
    print('Player 2 wins! ')

    #TIE
elif ((p1.upper() == 'ROCK' and p2.upper() == 'ROCK') or (p1.upper() == 'PAPER' and p2.upper() == 'PAPER') or (p1.upper() == 'SCISSORS' and p2.upper() == 'SCISSORS')):


    #PLAYER 1 WINS
elif p1.upper() == 'PAPER' and p2.upper() == 'ROCK':
        print('Player 1 wins! ')
elif p1.upper() == 'SCISSORS' and p2.upper() == 'PAPER':
        print('Player 1 wins! ')
elif p1.upper() == 'ROCK' and p2.upper() == 'SCISSORS':    
        print('Player 1 wins! ')









        