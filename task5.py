# Paste Task 5's solution here
#Task 5
# DO NOT delete this line
from diceroll import roll_the_dice

# TODO: Task 5
players_count = int(input("Please enter the number of players, at most 4 players:"))
players = ['Red', 'Blue', 'Green', 'White'][:players_count]
positions = [0] * players_count

# Initialize the positions of snakes and ladders
snake_heads = [25, 44, 65, 76, 99]
snake_tails = [6, 23, 34, 28, 56]  # Corrected snake tail positions
snakes = dict(zip(snake_heads, snake_tails))

ladder_bases = [8, 26, 38, 47, 66]
ladder_tops = [43, 39, 55, 81, 92]  # Corrected ladder top positions
ladders = dict(zip(ladder_bases, ladder_tops))

# Define functions for moving players
def move_player(position, player_name):
    roll = roll_the_dice() #Roll the dice using the imported function
    print(f"{player_name} rolled a {roll}")
    new_position = position + roll # Calculate new position based on roll
    
    # Check if the roll would cause the player to exceed 100
    if new_position <= 100:
        print(f"{player_name} moves from {position} to {new_position}")

        # Check for ladders or snakes at the new position and adjust the position accordingly
        if new_position in ladders:
            print(f"{player_name} found a ladder at {new_position}!")
            new_position = ladders[new_position]
            print(f"{player_name} climbs up to {new_position}")
        elif new_position in snakes:
            print(f"{player_name} landed on a snake at {new_position}!")
            new_position = snakes[new_position]
            print(f"{player_name} slides down to {new_position}")
    else:
        print(f"{player_name} rolled a {roll} but stays at {position} as it would exceed 100")
        return position # return the current position

    return new_position # return the new position

#Initialize winner variable
winner = None
while not winner:
    for i in range(players_count):  
        positions[i] = move_player(positions[i], players[i])  
        if positions[i] >= 100:
            winner = players[i]
            break
        
print(f"Player {winner} arrived at 100 points and wins the game!")

