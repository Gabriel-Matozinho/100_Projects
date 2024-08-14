import random

# Entrada do usuário
choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
Game = ['Rock', 'Paper', 'Scissors']

if choice < 0 or choice > 2:
    print("Type error")
else:
    # Escolha do jogador
    player_choice = Game[choice]
    print(f"You chose: {player_choice}")

    # Escolha do computador
    computer_choice = random.choice(Game)
    print(f"Computer chose: {computer_choice}")

    # Determinação do resultado
    if (player_choice == 'Rock' and computer_choice == 'Scissors') or \
       (player_choice == 'Paper' and computer_choice == 'Rock') or \
       (player_choice == 'Scissors' and computer_choice == 'Paper'):
        print("You win!")
    elif player_choice == computer_choice:
        print("It's a draw!")
    else:
        print("You lose!")
