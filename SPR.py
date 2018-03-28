# Sarvani Gaddipati
print('-------------------------------------------------------')
print('Welcome to Human vs. Computer in Scissors, Paper, Rock!')
print('-------------------------------------------------------')
print('Moves: choose scissors, paper or rock by typing in your selection.')
print('Rules: scissors cuts paper, paper covers rock and rock crushes scissors.')
print('Good luck!')
print('------------')
name = input('What is your name? ')
game_amount = int(input('How many games do you want to play? '))
cc = 0
hc = 0
results = {('paper', 'rock'): name,
       ('paper', 'paper'): 'draw',
       ('paper', 'scissors'): 'computer',
       ('scissors', 'scissors'): 'draw',
       ('scissors', 'paper'): name,
       ('scissors', 'rock'): 'computer',
       ('rock', 'scissors'): name,
       ('rock', 'paper'): 'computer',
       ('rock', 'rock'): 'draw'}
for i in range(game_amount):
    import random
    computer_move = random.choice(['rock', 'scissors', 'paper'])
    print(f'Hello {name}!')
    human_move = input('What is your move? scissors, paper or rock? ')
    human_move = human_move.lower()
    while human_move not in ['paper', 'scissors', 'rock', 'quit']:
        human_move = input('What is your move? scissors, paper or rock? ')
        human_move = human_move.lower()
    if human_move == 'quit':
        break
    print(f'{name} played: {human_move}, The computer played: {computer_move}')
    if results[human_move, computer_move] == 'draw':
        print('It is a draw!')
    elif results[human_move, computer_move] == 'computer':
        print('The computer won! Better luck next time.')
        cc = cc + 1
    elif results[human_move, computer_move] == name:
        print(f'{name} won! But can you beat the computer next time...?')
        hc = hc + 1
    game_amount = game_amount + 1
print('Game over!')
print(f'{name} won {hc} games')
print(f'Computer won {cc} games')
if cc < hc:
    print(f'Overall, {name} won!')
elif hc < cc:
    print('Overall, computer won!')
elif hc == cc:
    print('Overall it was a draw!')
    
