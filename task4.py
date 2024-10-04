# Paste Task 4's solution here
from diceroll import roll_the_dice

# Initialize player names and positions
p1_name = 'Red'
p2_name = 'Blue'
p1_position = 0
p2_position = 0

# Initialize the positions of snakes and ladders
snake_heads = [25, 44, 65, 76, 99]
snake_tails = [6, 23, 34, 28, 56]  # Corrected snake tail positions
snakes = dict(zip(snake_heads, snake_tails))

ladder_bases = [8, 26, 38, 47, 66]
ladder_tops = [43, 39, 55, 81, 92]  # Corrected ladder top positions
ladders = dict(zip(ladder_bases, ladder_tops))

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
        # If the result of rolling the dice would result in more than 100, keep the current position unchanged
        print(f"{player_name} rolled a {roll} but stays at {position} as it would exceed 100")
        return position # return the current position

    return new_position # return the new position

# Game loop
# The main game loop moves players in turn until one party reaches or exceeds position 100
while True:
    p1_position = move_player(p1_position, p1_name)
    if p1_position >= 100:
        break # Check did the player 1 win the game

    p2_position = move_player(p2_position, p2_name)
    if p2_position >= 100:
        break # CHeck did the player 2 win the game

# Determine the winner
winner = p1_name if p1_position == 100 else p2_name
print(f"Player {winner} has reached 100 and is the winner!")
