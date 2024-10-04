# Paste Task 6's solution here
from diceroll import roll_the_dice
from typing import Tuple

def initialise_game() -> Tuple[list, list, list, list, list, list]:
    # Function to initialize game setting

    #Initial player position
    players = ['Red', 'Blue', 'Green', 'White']
    positions = [0, 0, 0, 0]

    #Initial snak position
    snake_heads = [25, 44, 65, 76, 99]
    snake_tails = [6, 23, 34, 28, 56]

    ladder_bases = [8, 26, 38, 47, 66]
    ladder_tops = [43, 39, 55, 81, 92]

    return (players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops)
    
#Make sure the players int the number of the players should between 1 and 4
def get_num_players() -> int:
     while True:
        number_players = int(input("Please enter the number of players: "))
        if 1 <= number_players and number_players <= 4:
            return number_players
        else:
            print("Number of players should be between 1 and 4.")

#Managment gamPlay
def play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops) -> list:
    turn_counter = 0 #Keep track of the number of rounds played
    max_turns = 1000 # Set the limit, prevent infinite loops
    while turn_counter < max_turns:
        for i, player in enumerate(players):
            roll = roll_the_dice()
            new_position = positions[i] + roll

            if new_position > 100: # Prevent exceeding the game board
                continue

            #Check for snake
            if new_position in snake_heads:
                new_position = snake_tails[snake_heads.index(new_position)]

            #Check for ladder_bases
            if new_position in ladder_bases:
                new_position = ladder_tops[ladder_bases.index(new_position)]

            #Update the player's position after all checkes
            positions[i] = new_position

            if positions[i] == 100:#Check the winners
                return positions
        
        turn_counter += 1

    return positions

# Function to determine the winner based on position
def pick_winner(positions):
    for i, position in enumerate(positions):
        if position == 100:
            return i
    return -1

def main():
    players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops = initialise_game()
    final_positions = play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops)

    # Prompt the user to enter the number of players and adjust the player list accordingly
    number_players = get_num_players()
    players = players[:number_players]
    
    winner = pick_winner(final_positions)
    if winner != -1:
        print(f"The winner is {players[winner]}!")
    else:
        print("No winner has been determined.")

if __name__ == '__main__':
    main()
